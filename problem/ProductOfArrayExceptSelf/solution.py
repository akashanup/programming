"""Logic:
Create a prefix product array like, prefixProduct[i] = nums[0]*nums[1]*nums[2]....nums[i-1]
Iterate over the nums from right to left and kepp multiplying the prefixProduct[i] with the postfixProduct(product of nums from right eg, postfixProduct at ith index would be equal to nums[i]nums[i+1]...nums[n-1])
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [None] * n
        prefixProduct[0] = 1
        for i in range(1, n):
            prefixProduct[i] = nums[i-1] * prefixProduct[i-1]
        
        postfixProduct = nums[-1]
        for i in range(n-2, -1, -1):
            prefixProduct[i] *= postfixProduct
            postfixProduct *= nums[i]
        
        return prefixProduct
