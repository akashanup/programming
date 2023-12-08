class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        firstPermutation = sorted(A)
        if A == firstPermutation:
            return 1
        ans = 2
        nextPermutationList = self.__nextPermutation(list(firstPermutation))
        nextPermutation = "".join(nextPermutationList)
        while A != nextPermutation:
            ans += 1
            nextPermutationList = self.__nextPermutation(nextPermutationList)
            nextPermutation = "".join(nextPermutationList)
        return ans % 1000003

    def __nextPermutation(self, item):
        # Check for the index from right from where the array doesn't follow the descending order.
        i = len(item) - 2
        while i >= 0 and item[i + 1] <= item[i]:
            i -= 1

        # If any such index is found, then swap its value with the first greater element from the right.
        if i >= 0:
            j = len(item) - 1
            while j >= 0 and item[j] <= item[i]:
                j -= 1
            item[i], item[j] = item[j], item[i]

        # Reverse the further array items
        i += 1
        j = len(item) - 1
        while i < j:
            item[i], item[j] = item[j], item[i]
            i += 1
            j -= 1
        return item


print(Solution().findRank("DTNGJPURFHYEW"))
