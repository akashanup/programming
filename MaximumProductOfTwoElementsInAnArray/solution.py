class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        secondLargest = nums[1]
        if secondLargest > largest:
            largest, secondLargest = secondLargest, largest
        for i in range(2, len(nums)):
            num = nums[i]
            if num > largest:
                secondLargest = largest
                largest = num
            elif num > secondLargest:
                secondLargest = num
        return (largest-1) * (secondLargest-1)