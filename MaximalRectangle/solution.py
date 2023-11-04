class Solution:
    def nextSmallerElementIndex(self, heights):
        result = [-1] * len(heights)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result

    def previousSmallerElementIndex(self, heights):
        result = [-1] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(i)
        return result

    def largestRectangularAreaOfHistogram(self, heights):
        maxArea = 0
        nextSmallerHeightIndex = self.nextSmallerElementIndex(heights)
        previousSmallerHeightIndex = self.previousSmallerElementIndex(heights)
        for i, height in enumerate(heights):
            baseY = nextSmallerHeightIndex[i]
            if baseY == -1:
                baseY = len(heights)
            baseX = previousSmallerHeightIndex[i]
            base = baseY - baseX - 1
            area = height * base
            maxArea = max(maxArea, area)
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        heights = [0] * len(matrix[0])
        for row in range(len(matrix)):
            """
            Consider the heights of histogram is calculated based on the column values from the first row till current row.
            If for the current row, any column value is 0 then corresponding height would also be considered as 0 because we need only 1s in the rectangle.
            """
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0
            # Consider the current row as base. With respect to the base, calculate the area of rectangle with the height calculated above.
            area = self.largestRectangularAreaOfHistogram(heights)
            maxArea = max(maxArea, area)
        return maxArea
