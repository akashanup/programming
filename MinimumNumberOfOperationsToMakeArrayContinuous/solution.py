class Solution:
    def binarySearchFindCeil(self, nums, num):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == num:
                return mid + 1
            elif nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # Make `nums` as unique numbers and sort `nums`.
        nums = sorted(set(nums))

        ans = n
        for i, start in enumerate(nums):
            # Elements must continuous and must be in range from start to end
            end = start + n - 1
            # Find right insert position
            idx = self.binarySearchFindCeil(nums, end)
            existingPotentialElements = idx - i
            alteredPotentialElements = n - existingPotentialElements
            ans = min(ans, alteredPotentialElements)
        return ans
        
