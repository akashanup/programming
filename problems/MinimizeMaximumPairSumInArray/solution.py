class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        pairsSum = []
        while i < j:
            print((nums[i], nums[j]))
            pairsSum.append(nums[i] + nums[j])
            i += 1
            j -= 1
        return max(pairsSum)