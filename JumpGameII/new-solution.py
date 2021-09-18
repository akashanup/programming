import unittest


class Solution:
    def jump(self, nums, n):
        if n <= 1 or nums[0] == 0:
            return 0
        jumps = 1
        current = nums[0]
        farthest = nums[0]
        for num in range(1, n):
            if num == n-1:
                break
            current -= 1
            farthest -= 1
            if farthest < nums[num]:
                farthest = nums[num]
            if current == 0:
                jumps += 1
                current = farthest
            # Negative scenario when we fail to reach the end, simply return -1
            if farthest == 0:
                return -1
        return jumps


class Test(unittest.TestCase):
    def test_minJumpsToEnd_1(self):
        actual = Solution().jump([2, 3, 1, 1, 4], 5)
        expected = 2
        self.assertEqual(actual, expected)

    def test_minJumpsToEnd_2(self):
        actual = Solution().jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11)
        expected = 3
        self.assertEqual(actual, expected)

    def test_minJumpsToEnd_3(self):
        actual = Solution().jump([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 11)
        expected = 10
        self.assertEqual(actual, expected)

    def test_minJumpsToEnd_4(self):
        actual = Solution().jump([3, 2, 1, 0, 4], 5)
        expected = -1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
