"""
Time Complexity: O(N*LogN)
Space Complexity: O(N) NOTE: call stack is ignored.
Stable: Yes
In place: Not in the default implementation
"""


class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        self.__mergeSort(0, len(self.arr))
        return self.arr

    def __mergeSort(self, start, end):
        if end - start > 1:
            mid = start + ((end - start) // 2)
            self.__mergeSort(start, mid)
            self.__mergeSort(mid, end)
            self.__merge(start, mid, end)

    def __merge(self, start, mid, end):
        i, j, k = start, mid, 0
        mergeArray = [None] * (end - start)
        while i < mid and j < end:
            if self.arr[i] < self.arr[j]:
                mergeArray[k] = self.arr[i]
                i += 1
            else:
                mergeArray[k] = self.arr[j]
                j += 1
            k += 1
        # Check if any element is left
        while i < mid:
            mergeArray[k] = self.arr[i]
            i += 1
            k += 1
        while j < end:
            mergeArray[k] = self.arr[j]
            j += 1
            k += 1
        for l in range(len(mergeArray)):
            self.arr[start + l] = mergeArray[l]


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(MergeSort(array).sortArray())
