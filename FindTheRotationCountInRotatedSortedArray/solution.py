import unittest


class Solution:
    def findPivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if mid < end and nums[mid] > nums[mid + 1]:
                return mid
            elif mid > start and nums[mid] < nums[mid - 1]:
                return mid - 1
            elif nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return None

    def rotationCount(self, nums):
        pivotIndex = self.findPivot(nums)
        return (pivotIndex + 1) % len(nums) if pivotIndex else 0


class UnitTest(unittest.TestCase):
    def testRotationCount1(self):
        actual = Solution().rotationCount([15, 18, 2, 3, 6, 12])
        expected = 2
        self.assertEqual(actual, expected)

    def testRotationCount2(self):
        actual = Solution().rotationCount([7, 9, 11, 12, 5])
        expected = 4
        self.assertEqual(actual, expected)

    def testRotationCount3(self):
        actual = Solution().rotationCount([7, 9, 11, 12, 15])
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == "__main":
    unittest.main(verbosity=2)
