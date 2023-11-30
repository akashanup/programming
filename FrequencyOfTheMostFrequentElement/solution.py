"""
Logic:
    We will choose one number at a time and check which other numbers can be modified to be the current number.
    Since we can only increment a number, so we will check which all smaller numbers than the current number can be
    incremented to become the current number. If we sort the nums, then it would be easy to know which all numbers would
    be modified as these numbers would definitely be at the left of the current number.
    Now let's say for a number nums[i], we could modify x numbers on the left of nums[i] with using at most K
    operations.
    From the above statement we can conclude that-
    x * nums[i] would be equal to nums[i] + nums[i-1] + nums[i-2] + .. + nums[i-x]
    Now if this x is less than or equal to K than we have found one of the potential number with maximum frequency.
    If x > K then we would try to modify x-1 numbers on left.
    We just need to do this for all the numbers.
"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq = 0
        left = 0
        currentWindowSum = 0
        
        for right in range(len(nums)):
            target = nums[right]
            currentWindowSum += target
            
            while (right - left + 1) * target - currentWindowSum > k:
                currentWindowSum -= nums[left]
                left += 1
            
            maxFreq = max(maxFreq, right - left + 1)

        return maxFreq