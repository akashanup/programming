class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minWindow = len(nums)+1
        
        start, end = 0, 0
        windowSum = 0
        
        while end < len(nums):
            windowSum += nums[end]
            
            # Check for all window size till current index for which windowSum >= target. Find out the smallest such window size.
            while start <= end and windowSum >= target:
                minWindow = min(minWindow, end-start+1)
                windowSum -= nums[start]
                start += 1
            
            end += 1
                
        return minWindow if minWindow != len(nums)+1 else 0
