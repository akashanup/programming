class Solution:
    def combinations(self, unprocessed, processed=None):
        if processed is None:
            processed = []
        # Base Condition: Nothing to process, Empty input.
        if not unprocessed:
            return [processed]
        # Take the current item and recur for remaining.
        taken = self.combinations(unprocessed[1:], processed+[unprocessed[0]])
        # Reject the current item and recur for remaining.
        rejected = self.combinations(unprocessed[1:], processed)
        return taken + rejected

    def permutations(self, unprocessed, processed=None):
        if processed is None:
            processed = []
        # Base Condition: Nothing to process, Empty input.
        if not unprocessed:
            return [processed]
        answer = []
        for i in range(len(processed)+1):
            # Add the current item at ith index and recur for remaining.
            answer += self.permutations(unprocessed[1:], processed[:i]+[unprocessed[0]]+processed[i:])
        return answer


nums = [1, 2, 3]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
nums = [1, 2, 3, 4]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
