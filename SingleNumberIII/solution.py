class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for ele in nums:
            res = (res^ele)

        rmsb = (res & (-res))
        num1 = 0
        num2 = 0
        for ele in nums:
            if (ele&rmsb)!=0:
                num1 = num1^ele
            else:
                num2 = num2^ele
        return [num1,num2]
