"""

Logic:
    1. The idea is to group all the rectangles on the basis of their height in the increasing order of their length.
    2. Then for each point, find the minimum height first that would accommodate the y-coordinate of the point, then find the minimum length of rectangle that would accomodate the x-coordinate of point.
    3. If a potential rectangle is found which can accommodate the point, then the current rectangle and all the longer rectangle in the current height group would accomodate the point.
    3. For each point, repeat Step3 for all the higher rectangles than the minimum height rectangle.
"""


class Solution:
    def binarySearch(self, arr, target):
        left, right = 0, len(arr)
        ans = None
        while left < right:
            mid = left + ((right-left)//2)
            if arr[mid] >= target:
                # Potential answer found! Now try to minimize it iff possible.
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans
        
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Sort rectangles based on the lengths
        rectangles.sort()  
        # Group rectangles by their height in increasing order of their length
        lengths = {}
        for x,y in rectangles:
            if y in lengths:
                lengths[y].append(x)
            else:
                lengths[y] = [x]
        
        heights = sorted(list(lengths.keys()))
        
        count = [0] * len(points)
        
        for idx, point in enumerate(points):
            x, y = point
            # Get the  min height rectangle that would accommodate the y coordinate of current point.
            minHeightRectIdx = self.binarySearch(heights, y)
            if minHeightRectIdx is not None:
                for h in heights[minHeightRectIdx:]:
                    # Get the Min length rectangle that would accommodate the x coordinate of current point for all h height rectangles.
                    minLenRectIdx = self.binarySearch(lengths[h], x)
                    if minLenRectIdx is not None:
                        count[idx] += len(lengths[h]) - minLenRectIdx
        
        return count
