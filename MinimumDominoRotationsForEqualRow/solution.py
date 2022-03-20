"""
Logic:
    Since every domino has 2 numbers(top, bottom) on it so, so all the tops could be of one of those 2 numbers or all the bottoms could be of those two numbers.
    We will just try to calculate the number of rotations for making-
        All the tops as top
        All the bottoms as top
        All the tops as bottom
        All the bottoms as bottom
    Return the minimum of above four cases.
"""
import sys


class Solution:
    def getMinRotations(self, A, B, num):
        minRotations = 0
        for i in range(len(A)):
            if A[i] != num and B[i] != num:
                return sys.maxsize
            minRotations += int(A[i] != num)
        return minRotations

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        minRotations = sys.maxsize
        for num in [tops[0], bottoms[0]]:
            minRotations = min(minRotations, self.getMinRotations(tops, bottoms, num), self.getMinRotations(bottoms, tops, num))
        return -1 if minRotations == sys.maxsize else minRotations
