class BubbleSortRecursive:
    def __init__(self, arr):
        self.arr = arr

    def sortArray(self):
        self.__bubbleSort(len(self.arr) - 1, 0)
        return self.arr

    def __bubbleSort(self, r, c):
        if r == 0:
            return
        if c < r:
            if self.arr[c] > self.arr[c + 1]:
                self.arr[c], self.arr[c + 1] = self.arr[c + 1], self.arr[c]
            self.__bubbleSort(r, c + 1)
        else:
            self.__bubbleSort(r - 1, 0)


array = [5, 4, 2, 3, 1, 1, 5, 4, 2, 3]
print(BubbleSortRecursive(array).sortArray())
