"""
Logic:
    Lets say we have an fully arithmetic array of length n then the total number of arithmetic subarrays could be calculated as:
    Total number of subarrays of length 3 + Total number of subarrays of length 4 + ... + Total number of subarrays of length n. This is calculated by calcSlices function.
        Proof: Let's say the fully arithmetic array be [1,3,5,7,9].
        Total number of arithmetic subarrays of length 3 is 3 i.e, [1,3,5], [3,5,7], [5,7,9]
        Total number of arithmetic subarrays of length 4 is 2 i.e, [1,3,5,7], [3,5,7,9]
        Total number of arithmetic subarrays of length 5 is 1 i.e, [1,3,5,7,9]
        There the total number of arithmetic subarrays is 3+2+1 = 6
    Now we will iterate the array from 0th(let's say i) index and check till which further index(let's say j) the arithmetic property holds true.
    Once we find the above range i to j, we can calculate all the arithmetic subarrays within that range.
    Now we just need to find all those further ranges which fulfills the arithmetic property and calculate their arithmetic subarrays and return their sum.
"""


class Solution:
    def calcSlices(self, n):
        i = 3
        slices = 0
        while i <= n:
            slices += n-i+1
            i += 1
        return slices

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        slices = 0
        i = 0
        j = 1
        diff = nums[j] - nums[i]
        j += 1
        while j < len(nums):
            if nums[j] - nums[j-1] != diff:
                slices += self.calcSlices(j-i)
                i = j-1
                diff = nums[j] - nums[i]
            j += 1

        if nums[j-1] - nums[j-2] == diff:
            slices += self.calcSlices(j-i)
        return slices
