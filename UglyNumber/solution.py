class Solution:
    def nthUglyNumber(self, n):
        uglyNums = [0]*n
        uglyNums[0] = 1
        nextMultipleOf2 = 2
        nextMultipleOf3 = 3
        nextMultipleOf5 = 5
        i2 = i3 = i5 = 0
        for i in range(1, n):
            uglyNums[i] = min(nextMultipleOf2, nextMultipleOf3, nextMultipleOf5)
            if uglyNums[i] == nextMultipleOf2:
                i2 += 1
                nextMultipleOf2 = uglyNums[i2]*2
            if uglyNums[i] == nextMultipleOf3:
                i3 += 1
                nextMultipleOf3 = uglyNums[i3]*3
            if uglyNums[i] == nextMultipleOf5:
                i5 += 1
                nextMultipleOf5 = uglyNums[i5]*5
        return uglyNums[-1]
