class Solution:
    def trap(self, height: List[int]) -> int:
        walls = len(height)
        prefixMaxHeight = 0
        suffixMaxHeight = [0]*walls
        tempMax = 0
        for h in range(walls-1, -1, -1):
            tempMax = max(tempMax, height[h])
            suffixMaxHeight[h] = tempMax
        water = 0
        for h in range(walls):
            prefixMaxHeight = max(prefixMaxHeight, height[h])
            water += (min(suffixMaxHeight[h], prefixMaxHeight) - height[h])
        return water
        
