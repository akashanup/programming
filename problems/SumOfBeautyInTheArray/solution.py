class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * n
        maxI = 0
        for i in range(1, n - 1):
            maxI = max(maxI, nums[i - 1])
            if nums[i] > maxI:
                result[i] = 2
            elif nums[i] > nums[i - 1]:
                result[i] = 1
            else:
                result[i] = 0
        minI = 10 ** 5 + 1
        for i in range(n - 2, 0, -1):
            minI = min(minI, nums[i + 1])
            if nums[i] < minI:
                result[i] = min(result[i], 2)
            elif nums[i] < nums[i + 1]:
                result[i] = min(result[i], 1)
            else:
                result[i] = min(result[i], 0)
        return sum(result)
