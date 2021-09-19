import unittest


class Solution:
    def sort012(self, nums):
        lookup = {0: 0, 1: 0, 2: 0}
        for num in nums:
            lookup[num] += 1
        return ([0] * lookup[0]) + ([1] * lookup[1]) + ([2] * lookup[2])


class TestCase(unittest.TestCase):
    def test_sort012_1(self):
        actual = Solution().sort012([2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
        expected = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
