class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p, q = 0, 0
        result = []
        while p < len(nums1) and q < len(nums2):
            if nums1[p] == nums2[q]:
                result.append(nums1[p])
                p += 1
                q += 1
            elif nums1[p] > nums2[q]:
                q += 1
            else:
                p += 1
        return result
