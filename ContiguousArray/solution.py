"""
Logic:
    1. Let us say that we have a variable count whose value is updated while iterating the nums as whenever we encounter 1, count gets incremented by 1 and when 0 is encountered then count is decremented by 1.
    2. Now let us say that for an index i the value of count is x. While iterating the nums and performing the above operation for count we find that for an index j (j>i) the value of count again becomes x. This means that we have encountered the equal number of 1s and 0s as the increment and decrement in count gets nullified between indexes j and i.
    3. So we have a contiguous subarray nums[i:j+1] which has same number of 0s and 1s.
    4. Now we just need to apply the above logic and find the similar contiguous subarrays of maximum length.
    5. To store the value of count against each index of nums, we can use hashmap. So for any index j, if the value of count for index j is x and x is present in hashmap then we can simply find the length of contiguous subarrays as j - hashmap[x].
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1} # It is initialised in this way to handle the edge case like [0,1]
        count = 0
        maxLen = 0
        for index, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in hashmap:
                maxLen = max(maxLen, index-hashmap[count])
            else:
                hashmap[count] = index
        return maxLen
