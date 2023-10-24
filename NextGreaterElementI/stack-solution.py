class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        stack = [sys.maxsize]
        i = len(nums2)-1

        # Finding next greater element for all elements nums2 and storing in lookup.
        while i >= 0:
            while nums2[i] > stack[-1]:
                stack.pop()
            lookup[nums2[i]] = stack[-1]
            stack.append(nums2[i])
            i -= 1

        # Finding the next greater element for all elements of nums1 from lookup
        result = [-1]*len(nums1)
        for i, num in enumerate(nums1):
            result[i] = lookup[num] if lookup[num] != sys.maxsize else -1

        return result
