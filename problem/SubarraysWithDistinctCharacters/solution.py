class Solution:
    def distinctSubarraysLengthSum(self, nums):
        hashset = set()
        start, end = 0, 0
        lengthSum = 0
        while start < len(nums):
            while end < len(nums) and nums[end] not in hashset:
                hashset.add(nums[end])
                end += 1
            """
                If we know all elements in a subarray arr[i..j] are distinct, sum of all lengths of distinct element subarrays in this sub array is ((j-i+1)*(j-i+2))/2. 
                How? the possible lengths of subarrays are 1, 2, 3,……, j – i +1. So, the sum will be ((j – i +1)*(j – i +2))/2.
                We first find largest subarray (with distinct elements) starting from first element. 
                We count sum of lengths in this subarray using above formula. 
                For finding next subarray of the distinct element, we increment starting point, i and ending point, j unless (i+1, j) are distinct. 
                If not possible, then we increment i again and move forward the same way.
            """
            lengthSum += (end-start)*(end-start+1) // 2
            hashset.remove(nums[start])
            start += 1
        return lengthSum


print(Solution().distinctSubarraysLengthSum([1, 2, 3]))
print(Solution().distinctSubarraysLengthSum([1, 2, 1]))
print(Solution().distinctSubarraysLengthSum([1, 2, 3, 4]))
print(Solution().distinctSubarraysLengthSum([1, 2, 3, 4, 2]))
