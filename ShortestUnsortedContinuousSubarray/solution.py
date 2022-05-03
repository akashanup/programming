class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = None, None
        # First Pass: To find the last index of unsorted subarray of nums
        idx = 1
        currMax = nums[0]
        while idx < len(nums):
            if nums[idx] < currMax:
                end = idx
            currMax = max(currMax, nums[idx])
            idx += 1

        # Second Pass: To find the start index of unsorted subarray of nums
        idx = len(nums)-2
        currMin = nums[-1]
        while idx >= 0:
            if nums[idx] > currMin:
                start = idx
            currMin = min(currMin, nums[idx])
            idx -= 1

        if start is None:
            return 0

        return end - start + 1
