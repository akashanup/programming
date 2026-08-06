import unittest


class Solution:
    def sort012(self, nums):
        start = 0
        mid = 0
        end = len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[start], nums[mid] = nums[mid], nums[start]
                start += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
                # mid += 1
        return nums


class TestCase(unittest.TestCase):
    def test_sort012_1(self):
        actual = Solution().sort012([2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
        expected = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2]
        self.assertEqual(actual, expected)

    def test_sort012_2(self):
        actual = Solution().sort012([0, 2, 2, 1, 1, 0, 1])
        expected = [0, 0, 1, 1, 1, 2, 2]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
