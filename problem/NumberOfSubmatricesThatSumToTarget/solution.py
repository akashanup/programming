class Solution:

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        n = len(matrix)

        m = len(matrix[0])

        ans = 0

        for start in range(n):

            tempSum = [0] * m

            for i in range(start, n):

                for j in range(m):
                    tempSum[j] += matrix[i][j]

                ans += self.subSetSum(tempSum, target)

        return ans

    def subSetSum(self, arr, k):

        res = 0

        currSum = 0

        prefixSum = {0: 1}

        for n in arr:
            currSum += n

            diff = currSum - k

            res += prefixSum.get(diff, 0)

            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return res
