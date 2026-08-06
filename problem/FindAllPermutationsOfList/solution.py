class Solution:
    def getAllPermutations(self, nums):
        if len(nums) <= 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            # Generating all permutations where current is first element
            for permutation in self.getAllPermutations(remaining):
                permutations.append([current]+permutation)
        return permutations


print(Solution().getAllPermutations([1, 2, 3]))
