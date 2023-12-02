class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        Let us say nums = [x1,x2,x3] and result is [r1, r2, r3].
        As per the question,
        r1 = |x1-x1| + |x1-x2| + |x1-x3|,
        r2 = |x2-x1| + |x2-x2| + |x2-x3| and
        r3 = |x3-x1| + |x3-x2| + |x3-x3|.
        Since nums is sorted so r1 and r3 can be written as-
        r1 = x1-x1 + x2-x1 + x3-x1 => (x1+x2+x3) - 3*x1
        r3 = x3-x1 + x3-x2 + x3-x3 => 3*x3 - (x1+x2+x3)
        So if ith element is the first element than,
        r[i] would be, sum(nums) - len(nums)*nums[i] => eq1
        and if ith element is the last element than,
        r[i] would be, len(nums)*nums[i] - sum(nums) => eq2

        Now for any element at ith index, the above two equations can be used to find r[i] as =>
        r[i] would be eq2 (from first index till ith index) + eq1(from ith index till last index)
        """
        # Calculate prefix sum
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + nums[i]
        result = [None] * n
        for i in range(n):
            eq1 = prefixSum[-1] - prefixSum[i] - (n-i-1)* nums[i]
            eq2 = (i+1)*nums[i] - prefixSum[i]
            result[i] = eq1 + eq2
        return result