"""
Intuition
If you either think out of box or do a dry run for few of the cases than you will realize that meeting of ants and changing their directions doesn't makes any significance. So we just need to know which ant is farthest from the end of a plank from either side.

Approach
For the ants moving in left side, find the farthest ant from the left end of the plank. Max(left)
For the ants moving in right side, find the farthest ant from the right end of the plank. N - min(right)
Answer would be the max of above two scenarios.
"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = 0
        if left:
            l = max(left)
        r = 0
        if right:
            r = n - min(right)
        return max(l, r)