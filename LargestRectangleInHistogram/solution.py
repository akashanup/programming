"""
## Logic:
While traversing the list of heights from left to right, when we find a bar higher than the previous one, it means a rectangle with height equal to the height of that bar can be started there. And it can be extended (while keeping its height) at most until a bar with lower height is found, where it ends. With this in mind, we can iterate over the list of heights and add the corresponding index to a stack in each iteration.
Adding an element to the stack can be thought of as starting a rectangle.
But before adding the new element to the stack, we first remove all previous elements corresponding to previously "opened" rectangles with larger height, thus "closing" them.
The stack will always contain a sequence of indices corresponding to a non-decreasing sequence of heights. While "closing" a rectangle, we check if its area improves the score.

To close any rectangles that extended until the end of the list without additional checks after exiting the loop, it is convenient to append a bar with height zero at the end of the list. A rectangle with non-zero area can not contain a bar with height zero, therefore the stack is reset whenever such a bar is encountered. We also add a zero height bar at index -1 (in the stack initialization, not in the list itself). This way the stack will never get empty, since there is no need to ever "close" a zero height rectangle, and the required stack elements can be indexed. Whenever the stack is reset this property holds.
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        maxArea = 0
        for index, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = index - stack[-1] - 1
                maxArea = max(maxArea, h*w)
            stack.append(index)
        heights.pop()
        return maxArea
