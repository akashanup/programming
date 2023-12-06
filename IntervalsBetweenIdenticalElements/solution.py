"""
# Intuition
This question is very similar to [1685. Sum of Absolute Differences in a Sorted Array]
(https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/)

# Approach [Click Here](https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/solutions/4329588
/python-simple-intutive-solution-with-explanation-formula-derivation/) for the explanation

"""


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        lookup = {}
        for idx, num in enumerate(arr):
            if num not in lookup:
                lookup[num] = []
            lookup[num].append(idx)

        intervalsSum = {}
        for num, indexes in lookup.items():
            n = len(indexes)
            prefixSum = [i for i in indexes]
            for i in range(1, n):
                prefixSum[i] += prefixSum[i - 1]
            intervalSum = {}
            for i in range(n):
                eq1 = prefixSum[-1] - prefixSum[i] - (n - (i + 1)) * indexes[i]
                eq2 = (i + 1) * indexes[i] - prefixSum[i]
                intervalSum[indexes[i]] = eq1 + eq2
            intervalsSum[num] = intervalSum

        intervals = [-1] * len(arr)
        for idx, num in enumerate(arr):
            intervals[idx] = intervalsSum[num][idx]
        return intervals
