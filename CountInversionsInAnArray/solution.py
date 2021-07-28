class Solution:
    def merge(self, arr, tempArr, left, middle, right):
        i = left
        j = middle + 1
        k = left
        inversions = 0
        while i <= middle and j <= right:
            if arr[i] <= arr[j]:
                tempArr[k] = arr[i]
                i += 1
                k += 1
            else:
                # Since left and right subarrays are sorted, so all the remaining elements in left-subarray (a[i+1], a[i+2] … a[mid]) will be greater than a[j].
                inversions += (middle - i + 1)
                tempArr[k] = arr[j]
                j += 1
                k += 1
        while i <= middle:
            tempArr[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            tempArr[k] = arr[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            arr[i] = tempArr[i]
        return inversions

    def mergeSort(self, arr, tempArr, left, right):
        inversions = 0
        if left < right:
            middle = left + ((right - left) // 2)
            inversions += self.mergeSort(arr, tempArr, left, middle)
            inversions += self.mergeSort(arr, tempArr, middle + 1, right)
            inversions += self.merge(arr, tempArr, left, middle, right)
        return inversions

    def inversionCount(self, arr):
        n = len(arr)
        if n > 1:
            return self.mergeSort(arr, [0 for _ in range(n)], 0, n - 1)
        else:
            return 0


print(Solution().inversionCount([1, 20, 6, 4, 5]))
