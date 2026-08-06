class Solution:
    def nextSmallerItem(self, items):
        result = [-1] * len(items)
        stack = []
        for i in range(len(items) - 1, -1, -1):
            while stack and items[i] <= items[stack[-1]]:
                stack.pop()
            result[i] = stack[-1] if stack else -1
            stack.append(i)
        return result

    def previousSmallerItem(self, items):
        result = [-1] * len(items)
        stack = []
        for i in range(len(items)):
            while stack and items[i] <= items[stack[-1]]:
                stack.pop()
            result[i] = stack[-1] if stack else -1
            stack.append(i)
        return result

    def largestRectangleArea(self, heights: List[int]) -> int:
        nextSmallerHistogramIndex = self.nextSmallerItem(heights)
        previousSmallerHistogramIndex = self.previousSmallerItem(heights)

        largestArea = 0
        for index, height in enumerate(heights):
            baseY = nextSmallerHistogramIndex[index]
            baseY = baseY if baseY != -1 else len(heights)
            baseX = previousSmallerHistogramIndex[index]
            base = baseY - baseX - 1
            currentArea = height * base
            largestArea = max(largestArea, currentArea)

        return largestArea
