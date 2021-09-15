import unittest


class Solution:
    def binarySearch(self, nums, num):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == num:
                return mid
            elif nums[start] <= num < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1


class UnitTest(unittest.TestCase):
    def testbinarySearch1(self):
        actual = Solution().binarySearch(nums=[3, 4, 5, 6, 7, 8, 9, 10, 1, 2], num=1)
        expected = 8
        self.assertEqual(actual, expected)

    def testBinarySearch2(self):
        actual = Solution().binarySearch(nums=[3, 4, 5, 6, 7, 8, 9, 10, 1, 2], num=5)
        expected = 2
        self.assertEqual(actual, expected)

    def testBinarySearch3(self):
        actual = Solution().binarySearch(nums=[5, 6, 7, 8, 9, 10, 1, 2, 3], num=3)
        expected = 8
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
