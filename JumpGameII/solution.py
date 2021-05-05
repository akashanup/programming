class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if (n == 1 or nums[0] == 0):
            return 0
        
        jumps = 1;
        current = nums[0]
        farthest = nums[0]
        
        for i in range(1, n):
            if i == n-1:
                return jumps
            farthest = max(farthest, i + nums[i])
            if current == i:
                jumps += 1
                current = farthest
        return jumps