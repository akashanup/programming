import unittest


class Solution:
    def moveZerosToEnd(self, nums, n):
        p1, p2 = 0, 0
        # p1 will always be either 0 or nums[p1] = 0
        while p2 < n:
            if nums[p2] != 0:
                if p1 == p2:
                    p1 += 1
                    p2 += 1
                elif nums[p1] == 0:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 += 1
            else:
                p2 += 1
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
