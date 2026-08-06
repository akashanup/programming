from sortedcontainers import SortedList


class Solution:
    def findNearestIndex(self, arr, n, x):
        start = 0
        end = n
        mid = None
        while start <= end:
            mid = start + ((end - start) // 2)
            if arr[mid] == x:
                break
            elif arr[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        return mid

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x >= max(arr):
            return arr[n - k:]
        elif x <= min(arr):
            return arr[:k]
        else:
            # Find the index whose value is nearest to x
            mid = self.findNearestIndex(arr, n, x)
            if mid > 0:
                if arr[mid] == arr[mid - 1]:
                    start = mid
                    end = mid + 1
                else:
                    start = mid - 1
                    end = mid
            else:
                if arr[mid] == arr[mid + 1]:
                    start = mid - 1
                    end = mid
                else:
                    start = mid
                    end = mid + 1
            closestElements = SortedList([])
            i = 0
            while i < k:
                if start >= 0 and end < n:
                    if abs(arr[start] - x) < abs(arr[end] - x):
                        closestElements.add(arr[start])
                        start -= 1
                    elif abs(arr[end] - x) < abs(arr[start] - x):
                        closestElements.add(arr[end])
                        end += 1
                    else:
                        if arr[start] < arr[end]:
                            closestElements.add(arr[start])
                            start -= 1
                        else:
                            closestElements.add(arr[end])
                            end += 1
                elif start >= 0:
                    closestElements.add(arr[start])
                    start -= 1
                elif end < n:
                    closestElements.add(arr[end])
                    end += 1
                i += 1
            return closestElements
