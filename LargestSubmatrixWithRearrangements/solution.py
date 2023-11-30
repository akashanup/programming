class Solution:
    def __nextSmallerElementIndex(self, nums):
        result = [-1] * len(nums)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if row > 0 and matrix[row-1][col] > 0 and matrix[row][col] == 1:
                    matrix[row][col] += matrix[row-1][col]
        """
        Since we can rearrange the columns of matrix so let us sort each row of the matrix.
        Sorting ensures that we would get the largest submatrix.
        Now after sorting, the problem boils down to largest rectangular area of histogram where each row would act as a base and column values would act as heights of histogram bars.
        """

        maxArea = 0
        for row in matrix:
            # Here we do not need to find the previous smaller element index because row is sorted here so we can conclude that for current height[i], all the heights at left of i would be greater that height[i] hence the base of rectangle could be extended to the extreme left of i.
            row.sort(reverse=True)
            nextSmallerIdx = self.__nextSmallerElementIndex(row)
            for b, height in enumerate(row):
                base = nextSmallerIdx[b]
                if base == -1:
                    base = n
                area = base * row[b]
                maxArea = max(area, maxArea)
        return maxArea
