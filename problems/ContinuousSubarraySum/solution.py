from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Initialise the hashmap with a reminder 0 as a key and -1 as value for edge cases like -
        nums = [4,2], k = 6
        """
        lookup = {0: -1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            rem = currSum % k
            # if the remainder occurs for the first time, save its index.
            if rem not in lookup:
                lookup[rem] = i
            else:
                """It means that the current remainder is already present in hashmap and we have found that reminder again. 
                Now the current reminder can be found again if we have added the values whose sum is a multiple ok k because then only we can get the same reminder again.
                """
                # if the subarray size is at least two
                if i-lookup[rem] > 1:
                    return True
        return False


print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
