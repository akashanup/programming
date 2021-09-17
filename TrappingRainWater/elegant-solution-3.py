class Solution:
    def trap(self, height: List[int]) -> int:
        walls = len(height)
        water = 0
        maxHeight = max(height)
        maxHeightIndex = height.index(maxHeight)
        leftMaxHeight = 0
        for h in range(maxHeightIndex):
            leftMaxHeight = max(leftMaxHeight, height[h])
            water += (min(maxHeight, leftMaxHeight) - height[h])
        rightMaxHeight = 0
        for h in range(walls - 1, maxHeightIndex, -1):
            rightMaxHeight = max(rightMaxHeight, height[h])
            water += rightMaxHeight - height[h]
            '''
                This is not used because rightMaxHeight will always be less than maxHeight for this dataset
                water += (min(maxHeight, rightMaxHeight) - height[h])
            '''
        return water

