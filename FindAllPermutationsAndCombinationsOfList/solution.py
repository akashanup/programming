class Solution:
    def combinations(self, unprocessed, processed=[]):
        if not unprocessed:
            return [processed]
        return self.combinations(unprocessed[1:], processed+[unprocessed[0]]) + self.combinations(unprocessed[1:], processed)

    def permutations(self, unprocessed, processed=[]):
        if not unprocessed:
            return [processed]
        answer = []
        for i in range(len(processed)+1):
            answer += (self.permutations(unprocessed[1:], processed[:i]+[unprocessed[0]]+processed[i:]))
        return answer


nums = [1, 2, 3]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
nums = [1, 2, 3, 4]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
