class Solution:
    def maximumGap(self, A):
        n = len(A)
        arr = []
        for i in range(n):
            arr.append([A[i], i])
        arr.sort(key=lambda x: x[0])
        ans = 0
        minIndex = 999999
        for i in range(len(arr)):
            minIndex = min(minIndex, arr[i][1])
            ans = max(ans, arr[i][1] - minIndex)
        return ans

