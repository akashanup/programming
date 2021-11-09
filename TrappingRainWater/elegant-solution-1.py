class Solution:
    def trap(self, height: List[int]) -> int:
        walls = len(height)
        prefixMaxHeight = [0]*walls
        suffixMaxHeight = [0]*walls
        tempMax = 0
        for h in range(walls):
            tempMax = max(tempMax, height[h])
            prefixMaxHeight[h] = tempMax
        tempMax = 0
        for h in range(walls-1, -1, -1):
            tempMax = max(tempMax, height[h])
            suffixMaxHeight[h] = tempMax
        water = 0
        '''
            height          = [0,1,0,2,1,0,1,3,2,1,2,1]
            prefixMaxHeight = [0,1,1,2,2,2,2,3,3,3,3,3]
            suffixMaxHeight = [3,3,3,3,3,3,3,3,2,2,2,1]
            min             = [0,1,1,2,2,2,2,3,2,2,2,1]
            min - height    = [0,0,1,0,1,2,1,0,0,1,0,0]
            water           = sum(min-height) = 6
        '''
        for h in range(walls):
            water += (min(suffixMaxHeight[h], prefixMaxHeight[h]) - height[h])
        return water

