class Solution:
    def dpFn(self, nums, numsLen, n, splitAmount, split, lookup):
        key = tuple(split)
        if key not in lookup:
            if n == numsLen:
                lookup[key] = split[0] == split[1] == split[2] == splitAmount
            else:
                for i in range(3):
                    if split[i] + nums[n] <= splitAmount:
                        split[i] = split[i] + nums[n]
                        if self.dpFn(nums, numsLen, n + 1, splitAmount, split, lookup):
                            lookup[key] = True
                            break
                        split[i] = split[i] - nums[n]
                if key not in lookup:
                    lookup[key] = False
        return lookup[key]

    def evenSplit3(self, nums):
        nums = sorted(nums, reverse=True)
        numsSum = sum(nums)
        if numsSum % 3:
            return False
        splitAmount = numsSum // 3
        if nums[0] > splitAmount:
            return False
        return self.dpFn(nums, len(nums), 0, numsSum // 3, [0, 0, 0], {})
