import unittest


class Solution:
    def moveZerosToEnd(self, nums, n):
        nonZeroNums = 0
        for num in nums:
            if num != 0:
                nums[nonZeroNums] = num
                nonZeroNums += 1
        for i in range(nonZeroNums, n):
            nums[i] = 0
        return nums


class Test(unittest.TestCase):

    def test_MoveZerosToEnd1(self):
        actual = Solution().moveZerosToEnd([1, 3, 0, 0, 4, 0, 9], 7)
        expected = [1, 3, 4, 9, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_MoveZerosToEnd2(self):
        actual = Solution().moveZerosToEnd([0, 1, 0, 3, 12], 5)
        expected = [1, 3, 12, 0, 0]
        self.assertEqual(actual, expected)

    def test_MoveZerosToEnd3(self):
        actual = Solution().moveZerosToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9], 13)
        expected = [1, 9, 8, 4, 2, 7, 6, 9, 0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
