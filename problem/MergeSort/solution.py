import unittest

class Solution:
    def merge(self, nums1, nums2):
        i = 0
        j = 0
        mergeArray = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mergeArray.append(nums1[i])
                i += 1
            else:
                mergeArray.append(nums2[j])
                j += 1
        while i < len(nums1):
            mergeArray.append(nums1[i])
            i += 1
        while j < len(nums2):
            mergeArray.append(nums2[j])
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


class Test(unittest.TestCase):
    def testMergeSort1(self):
        arr = [12, 11, 13, 5, 6, 7]
        actual = Solution().mergeSort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)

    def testMergeSort2(self):
        arr = [8, 4, 3, 35, 6, 10, 13]
        actual = Solution().mergeSort(arr)
        expected = sorted(arr)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
