class SelectionSortRecursive:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        self.__selectionSort(len(self.arr), 0, 0)
        return self.arr

    def __selectionSort(self, r, c, maxValIdx):
        if r == 0:
            return
        if c < r:
            if self.arr[c] > self.arr[maxValIdx]:
                self.__selectionSort(r, c + 1, c)
            else:
                self.__selectionSort(r, c + 1, maxValIdx)
        else:
            self.arr[r-1], self.arr[maxValIdx] = self.arr[maxValIdx], self.arr[r-1]
            self.__selectionSort(r - 1, 0, 0)


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(SelectionSortRecursive(array).sortArray())
