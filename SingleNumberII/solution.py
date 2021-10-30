class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
            This question can be solved using bit manipulation.
            If any number is occuring 3 times then the count of every bit of that number will also be 3.
            For example, let's say we have 5,5,5 then,
            Binary representation is 101,101,101.
            Now if we see the count of 0th, 1st and 2nd bit, it will all be 3.
            Now if another number occurs, let's say 4(100) then the count of every bit will be:
                0th: 3
                1st: 3
                2nd: 4

            So by using the above logic if we get a count of each bit for all the numbers and take modulo of 3 for each bit then the resulting number would be our answer.
            Like in above example, count of each bit became 4, 3, 3 and if we take % 3 then it will become 1,0,0 and 100 is 4(our answer).

        """
        res = 0
        for i in range(32):
            count = 0
            for n in nums:
                temp = n >> i
                temp = temp & 1
                count += temp
            rem = count % 3
            if i == 31 and rem:  # must handle the negative case
                res -= 1 << 31
            else:
                res |= rem << i
        return res
