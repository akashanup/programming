class Solution:
    def pythagoreanTriplet(self, arr):
        arr = [i**2 for i in arr]
        arr.sort(reverse=True)
        arrLen = len(arr)
        for i in range(arrLen - 2):
            start = i + 1
            end = arrLen - 1
            while start < end:
                if arr[i] == (arr[start]) + (arr[end]):
                    return True
                if arr[i] > (arr[start]) + (arr[end]):
                    end -= 1
                else:
                    start += 1
        return False

