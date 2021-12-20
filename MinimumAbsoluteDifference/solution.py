import sys


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = sys.maxsize
        output = []
        for i in range(len(arr)-1):
            diff = abs(arr[i+1] - arr[i])
            if diff < minDiff:
                minDiff = diff
                output = [[arr[i], arr[i+1]]]
            elif diff == minDiff:
                output.append([arr[i], arr[i+1]])
        return output
