class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            if end - start < 2:
                return start if arr[start] > arr[end] else end
            mid = start + ((end - start) // 2)
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

