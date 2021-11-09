class Solution:
    # Counting sort based on digits place like unit digit, tens digit etc
    def countingSort(self, arr, digitPlace):
        # print(arr)
        lookup = [0] * 10
        for i in arr:
            index = i // digitPlace
            lookup[index % 10] += 1
        # print(lookup)
        for i in range(1, 10):
            lookup[i] += lookup[i - 1]
        # print(lookup)
        sortedArr = [None] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            index = arr[i] // digitPlace
            sortedArr[lookup[index % 10] - 1] = arr[i]
            lookup[index % 10] -= 1
        # print(sortedArr)
        return sortedArr

    def radixSort(self, arr):
        maxArr = max(arr)
        digitPlace = 1
        while maxArr > 0:
            arr = self.countingSort(arr, digitPlace)
            digitPlace *= 10
            maxArr //= 10
        arr = [i for i in arr if i < 0] + [i for i in arr if i >= 0]
        return arr


print(Solution().radixSort([92, 17, 0, -1, -536, -992, -516, -745, 46, 48, 42]))
