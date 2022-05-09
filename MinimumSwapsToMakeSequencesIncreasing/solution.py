"""Logic
1. Instead of checking everytime the entire array to be strictly increasing, we could check at each index whether the element is greater than its previous index or not. If it is then the array is strictly increasing till this index.
2. So if the index reaches the end of array it means the array is strictly increasing.
3. Now for each index,
    We will check whether the element at the current index for both the arrays can be swapped or not. If it can be swapped then we have one swap and then we can recur for further indexes.
    We also need to check whether can we go for further recurrence without swapping
4. The minimum of above two scenarios would be the answer.
"""


class Solution:
    def dp(self, nums1, nums2, prev1, prev2, i, swapped, lookup):
        if i == len(nums1):
            return 0

        key = (i, swapped)
        if key not in lookup:
            minSwaps = sys.maxsize
            # Swap
            if nums2[i] > prev1 and nums1[i] > prev2:
                minSwaps = 1 + self.dp(nums1, nums2, nums2[i], nums1[i], i + 1, 1, lookup)
            # Dont swap
            if nums2[i] > prev2 and nums1[i] > prev1:
                minSwaps = min(minSwaps, self.dp(nums1, nums2, nums1[i], nums2[i], i + 1, 0, lookup))
            lookup[key] = minSwaps
        return lookup[key]

    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        return self.dp(nums1, nums2, -1, -1, 0, 0, {})
