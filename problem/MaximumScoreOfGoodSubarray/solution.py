class Solution:
    def getPreviousSmallerItemIndexes(self, nums):
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result

    def getNextSmallerItemIndexes(self, nums):
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result

    def maximumScore(self, nums: List[int], k: int) -> int:
        previousSmallerItemIndexes = self.getPreviousSmallerItemIndexes(nums)
        nextSmallerItemIndexes = self.getNextSmallerItemIndexes(nums)

        maxScore = 0
        for i, num in enumerate(nums):
            previousSmallerItemIndex = previousSmallerItemIndexes[i]
            nextSmallerItemIndex = nextSmallerItemIndexes[i]
            if nextSmallerItemIndex == -1:
                nextSmallerItemIndex = len(nums)
            # Now it is clear that num is the minimum in between previousSmallerItemIndex+1 and nextSmallerItemIndex-1
            # So if k lies in between this, then we have a good subarray
            if previousSmallerItemIndex + 1 <= k <= nextSmallerItemIndex - 1:
                maxScore = max(maxScore, ((nextSmallerItemIndex - 1) - (previousSmallerItemIndex + 1) + 1) * num)
        return maxScore
