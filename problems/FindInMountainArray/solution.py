# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findPeakIndex(self, arr):
        start = 0
        end = arr.length() - 1
        while start < end:
            mid = start + ((end - start) // 2)
            if arr.get(mid) > arr.get(mid+1):
                # We are on the decreasing part of arr. So, arr[mid] might be a potential answer but answer may be present to left of mid also. So we need to look for left of mid also.
                end = mid
            else:
                # We are on the increasing part of arr. So, the answer would definitely be present at right ride of mid.
                start = mid + 1
        # The loop terminates when start == end. This also means that start(or end) will have the peak element as well because the if else inside the loop converges towards the peak element.
        return start

    def binarySearch(self, arr, start, end, target, isAscending):
        while start <= end:
            mid = start + ((end - start) // 2)
            if arr.get(mid) == target:
                return mid
            elif isAscending:
                if target < arr.get(mid):
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > arr.get(mid):
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find the index from which the mountain_arr will be broken into pair of ascending and decinding arrays.
        # Apply Binary Search to both arrays as required.
        peakIndex = self.findPeakIndex(mountain_arr)
        targetIndex = self.binarySearch(mountain_arr, 0, peakIndex, target, True)
        return targetIndex if targetIndex != -1 else self.binarySearch(mountain_arr, peakIndex+1, mountain_arr.length()-1, target, False)
