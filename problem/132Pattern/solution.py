class Solution:
    def previousMinimum(self, nums):
        prevMin = [None] * len(nums)
        prevMin[0] = nums[0]
        for i in range(1, len(nums)):
            prevMin[i] = min(nums[i], prevMin[i-1])
        return prevMin

    def previousGreater(self, nums):
        stack = [[sys.maxsize, -1]]
        greater = [None] * len(nums)
        for i in range(len(nums)):
            while nums[i] >= stack[-1][0]:
                stack.pop()
            greater[i] = stack[-1][1]
            stack.append([nums[i], i])
        return greater

    def find132pattern(self, nums: List[int]) -> bool:
        prevGreater = self.previousGreater(nums)
        prevMin = self.previousMinimum(nums)

        # nums[i] represents two
        for i in range(len(nums)-1, -1, -1):
            # nums[j] represents three
            # prevMin[j] represents one
            j = prevGreater[i]
            # three is greater than two is ensured by previousGreater function.
            # If two isn't the greatest from left and, one < three and one < two
            if j != -1 and prevMin[j] < nums[j] and prevMin[j] < nums[i]:
                return True
        return False


