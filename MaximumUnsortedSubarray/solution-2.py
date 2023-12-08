class Solution:
    def subUnsort(self, A):
        b = sorted(A)  # sorted form of A is B
        if A == b:
            return [-1]
        else:
            # LIST OF ALL POINTS WHICH ARE NOT IN THE CORRECT PLACE
            L = [i for i in range(len(A)) if A[i] != b[i]]
            return [min(L), max(L)]


print(Solution().subUnsort([1, 3, 2, 4, 5]))
print(Solution().subUnsort([1, 11, 13, 12, 6, 14, 15]))
