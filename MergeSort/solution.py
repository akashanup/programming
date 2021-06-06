class Solution:
    def merge(self, num1, num2):
        i = 0
        j = 0
        mergeArray = []
        while i < len(num1) and j < len(num2):
            if num1[i] > num2[j]:
                mergeArray.append(num1[i])
                i += 1
            else:
                mergeArray.append(num2[j])
                j += 1
        while i < len(num1):
            mergeArray.append(num1[i])
            i += 1
        while j < len(num2):
            mergeArray.append(num2[j])
            j += 1
        return mergeArray

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            h1 = self.mergeSort(arr[:mid])
            h2 = self.mergeSort(arr[mid:])
            return self.merge(h1, h2)
        else:
            return arr


print(Solution().mergeSort([12, 11, 13, 5, 6, 7]))
