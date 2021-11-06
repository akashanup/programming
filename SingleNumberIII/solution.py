class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
            We will be needing xor of the elements of the complete array in two passes.

            As we know the two numbers appearing once will differ atleast one bit

            Eg:- Let 1st number be 1 and 2nd be 5
            1 => 0001
            5 => 0101
            1 and 5 differ at 3rd bit
            So, we need to find the one bit at which numbers differ, so that we can divide the array into two groups

            Eg :- Let array be [1,3,3,4,4,5,6,6,7,7]
            We can observe that the two numbers coming once are 1 and 5, bit at which
            1 and 5 differ are 3rd bit
            So, number :- 1 ,3rd bit is 0 and number 5, 3rd bit is 1
            Now we need to divide the array into two groups with numbers at 3rd bit == 0 as 1st group and numbers with 3rd bit==1 into second

            Group 1 => [1,1,3]  //1 and 3 are having 3rd bit as 0
            Group 2 => [4,4,5,6,6,7,7]  //4,5,6,7 are having 3rd bit as 1
            Now xor into respective groups will give us the two numbers.
        """
        res = 0
        for ele in nums:
            res = (res ^ ele)

        rmsb = (res & (-res))
        num1 = 0
        num2 = 0
        for ele in nums:
            if (ele & rmsb) != 0:
                num1 = num1 ^ ele
            else:
                num2 = num2 ^ ele
        return [num1, num2]
