class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            item = arr[i]
            j = i - 1
            while j >= 0 and item < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = item
        return arr


print(Solution().insertionSort([5, 8, 12, 9, 21, 0, 3, -1, 3, 4, -2]))
