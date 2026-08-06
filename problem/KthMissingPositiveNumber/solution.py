class Solution:
    def binarySearch(self, arr, target):
        start = 0
        end = len(arr) -1
        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
        
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missingCount = 0
        for i in range(1, len(arr)+k+1):
            if not self.binarySearch(arr, i):
                missingCount += 1
                if missingCount == k:
                    return i
            
            
