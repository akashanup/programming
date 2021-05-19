class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        numsLen = len(nums)
        median = nums[numsLen // 2] if numsLen % 2 else ((nums[numsLen // 2] + nums[(numsLen - 1) // 2]) // 2)
        moves = 0
        for i in nums:
            moves += abs(median - i)
        return moves
