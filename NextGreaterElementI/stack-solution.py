class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        stack = []

        # Finding next greater element for all elements nums2 and storing in lookup.
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            lookup[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        # Finding the next greater element for all elements of nums1 from lookup
        result = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            result[i] = lookup[num]

        return result
