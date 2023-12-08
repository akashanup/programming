class Solution:
    def subUnsort(self, A):
        lenA = len(A)
        B = A.copy()
        i = 1
        s, e = None, None
        while i < lenA:
            if A[i] < A[i - 1]:
                e = i
                A[i], A[i - 1] = A[i - 1], A[i]
            i += 1
        i = lenA - 2
        while i >= 0:
            if B[i] > B[i + 1]:
                s = i
                B[i], B[i + 1] = B[i + 1], B[i]
            i -= 1
        return [s, e] if s is not None else [-1]


print(Solution().subUnsort([1, 3, 2, 4, 5]))
print(Solution().subUnsort([1, 11, 13, 12, 6, 14, 15]))
