class Solution:
    def merge(self, nums1, nums2):
        i, j = 0, 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        return merged

    def mergeSort(self, nums, i, j):
        if i < j:
            mid = i + ((j - i) // 2)
            m1 = self.mergeSort(nums, i, mid)
            m2 = self.mergeSort(nums, mid+1, j)
            return self.merge(m1, m2)
        return nums[i:j+1]

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums)-1)
    
