"""
Logic:
We need to iterate the list from the beginning and try to find the index (say i) from where the list fails its sequence.
It means that A[i-1] > A[i].
So if we find the correct index for A[i-1] as per sorted A then we can say that we have found the last index of
current unsorted subarray.
Remember that there could be many such unsorted subarrays. Hence, we need to iterate all the unsorted subarrays to find
the last index which would guarantee that the last index would be the last index of final maximum unsorted subarray.

Now we need to iterate the list from end to find the first index for which the array fails its sequence. We could use
the above logic to find the start index of final maximum unsorted subarray.
"""


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
