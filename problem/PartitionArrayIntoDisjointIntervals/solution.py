class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        numsLen = len(nums)
        maxArr = [None] * numsLen
        minArr = [None] * numsLen
        maxNum = 0
        minNum = 10 ** 6
        for i in range(numsLen):
            # Building minArr from end
            if minNum > nums[numsLen - 1 - i]:
                minNum = nums[numsLen - 1 - i]
            minArr[numsLen - 1 - i] = minNum
            # Build maxArr from start
            if maxNum < nums[i]:
                maxNum = nums[i]
            maxArr[i] = maxNum
        for i in range(numsLen):
            '''
                Partitioning Index will be the index where maxArr is less then or equal to minArr of next index.
                Because till that index, that element and every element left to it would be less then or equal to every element present right to it.
                (minArr[i+1] will not give an index out of range exception because It is guaranteed there is at least one way to partition nums as described.) 
            '''
            if maxArr[i] <= minArr[i + 1]:
                return i + 1
