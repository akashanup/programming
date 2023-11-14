class Solution:
    def combinations(self, nums):
        return self.__combinations([], nums, 0)

    def permutations(self, nums):
        return self.__permutations([], nums, 0)

    def __combinations(self, processed, unprocessed, u):
        # Base Condition: Nothing to process, Empty input.
        if u == len(unprocessed):
            return [processed]
        currentItem = unprocessed[u]
        # Take the current item and recur for remaining.
        taken = self.__combinations(processed+[currentItem], unprocessed, u+1)
        # Reject the current item and recur for remaining.
        rejected = self.__combinations(processed, unprocessed, u+1)
        return taken + rejected

    def __permutations(self, processed, unprocessed, u):
        # Base Condition: Nothing to process, Empty input.
        if u == len(unprocessed):
            return [processed]
        currentItem = unprocessed[u]
        answer = []
        for i in range(len(processed)+1):
            answer += self.__permutations(processed[:i]+[currentItem]+processed[i:], unprocessed, u+1)
        return answer


nums = [1, 2, 3]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
nums = [1, 2, 3, 4]
print("Combinations:", Solution().combinations(nums))
print("Permutations:", Solution().permutations(nums))
