class Solution:
    def binarySearch(self, nums, num):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == num:
                return mid
            elif nums[mid] < num:
                left = mid + 1
            else:
                right = mid -1
        return - 1

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        # Now length of nums1 is less than or eqaul to length of nums2
        nums2.sort()
        result = []
        i = 0
        lenNums1 = len(nums1)
        while i < lenNums1:
            nums2Index = self.binarySearch(nums2, nums1[i])
            if nums2Index != -1:
                result.append(nums1[i])
                nums2.pop(nums2Index)
            i += 1
        return result
