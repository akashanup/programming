"""
If we closely look at the patter for let's say till n = 4:
    0
   0|1
  01|10
0110|1001

Then we can see that whatever lies at right side of the | is the complement of whatever lies at left side of | for each row > 1.

It also means that for any row the value of any index i on the left side has its complement value at the corresponding index j on the right side.

For example, for 4th row let's say the index range is from 1-4 and at right side the index range is from 5-8. Now,
- the value at index 5 = 1-value at index 1
- the value at index 6 = 1-value at index 2
- the value at index 7 = 1-value at index 3
- the value at index 8 = 1-value at index 4

So from the above pattern we can say that the value of index i in left side = 1- value at index (mid+i) where mid is half of length of the row.

Now if we need to find the value at index k for row n, we can say that if k lies in right side then the value would definitely be the value at k-mid index(which would be on the left side.)

So we just need to know the values at left side.
Now if you see the above pattern carefully then you will also notice that the value present on the left side for the nth row is same as (n-1)th row itself.

Based on the above observation, recurrence relations can be formed -
- leftValues(nth row) = (n-1)th row
- and if k lies at left side then
  - value at kth index for leftValues(nth row) = value at kth index for (n-1)th row
- and if k lies at right side then
  - value at kth index for rightValues(nth row) = value at (k-mid)th index for leftValues(nth row) = value at (k-mid)th index for (n-1)th row.
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        nThRowDigitCount = 2 ** (n - 1)
        mid = nThRowDigitCount // 2
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)