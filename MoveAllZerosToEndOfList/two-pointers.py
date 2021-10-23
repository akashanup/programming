import unittest


class Solution:
    def moveZerosToEnd(self, nums, n):
        zero, nonzero = 0, 0
        while zero < len(nums) and nonzero < len(nums):
            if nums[zero] != 0:
                zero += 1
            else:
                if zero < nonzero and nums[nonzero] != 0:
                    nums[zero], nums[nonzero] = nums[nonzero], nums[zero]
                nonzero += 1
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
