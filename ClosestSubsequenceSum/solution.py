class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        mid = len(nums) // 2
        subSum1 = self.__getSubsequences(nums[:mid], 0, 0)
        subSum2 = self.__getSubsequences(nums[mid:], 0, 0)
        subSum2.sort()
        ans = sys.maxsize
        for ss in subSum1:
            counterPart = goal - ss
            idx = self.__binarySearchLeft(subSum2, counterPart)
            if idx < len(subSum2):
                ans = min(ans, abs(counterPart - subSum2[idx]))
            if idx > 0:
                ans = min(ans, abs(counterPart - subSum2[idx - 1]))
        return ans

    def __getSubsequences(self, nums, i, subSum):
        if i == len(nums):
            return [subSum]
        current = nums[i]
        taken = self.__getSubsequences(nums, i + 1, subSum + current)
        ignored = self.__getSubsequences(nums, i + 1, subSum)
        return taken + ignored

    def __binarySearchLeft(self, nums, target):
        s, e = 0, len(nums) - 1
        ans = -1
        while s <= e:
            m = s + ((e - s) // 2)
            if nums[m] >= target:
                ans = m
                e = m - 1
            else:
                s = m + 1
        return ansclass Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        mid = len(nums) // 2
        subSum1 = self.__getSubsequences(nums[:mid], 0, 0)
        subSum2 = self.__getSubsequences(nums[mid:], 0, 0)
        subSum2.sort()
        ans = sys.maxsize
        for ss in subSum1:
            counterPart = goal - ss
            idx = self.__binarySearchLeft(subSum2, counterPart)
            if idx < len(subSum2):
                ans = min(ans, abs(counterPart-subSum2[idx]))
            if idx > 0:
                ans = min(ans, abs(counterPart-subSum2[idx-1]))
        return ans


    def __getSubsequences(self, nums, i, subSum):
        if i == len(nums):
            return [subSum]
        current = nums[i]
        taken = self.__getSubsequences(nums, i+1, subSum+current)
        ignored = self.__getSubsequences(nums, i+1, subSum)
        return taken + ignored

    def __binarySearchLeft(self, nums, target):
        s, e = 0, len(nums)-1
        ans = -1
        while s <= e:
            m = s + ((e-s)//2)
            if nums[m] >= target:
                ans = m
                e = m-1
            else:
                s = m+1
        return ans