class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        for i in nums1:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        result = []
        for i in nums2:
            if i in lookup and lookup[i] > 0:
                result.append(i)
                lookup[i] -= 1
        return result
