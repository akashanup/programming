class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.numsSum = sum(nums)

    def update(self, index, val):
        if val >= self.nums[index]:
            self.numsSum += (val - self.nums[index])
        else:
            self.numsSum -= (self.nums[index] - val)
        self.nums[index] = val

    def sumRange(self, left, right):
        return self.numsSum - sum(self.nums[:left]) - sum(self.nums[right + 1:])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
