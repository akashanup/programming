"""
Logic:
Let's start by looking at the first character.
If the first character is X, all permutations that had the first character less than X would come before this
permutation when sorted lexicographically.
We also know that the number of permutations with a character C as the first character
    = number of permutations possible with remaining N-1 character = (N-1)!
Then the problem reduces to finding the rank of the permutation after removing the first character from the set.
Hence,
rank = number of characters less than first character * (N-1)!
    + rank of permutation of string with the first character removed (Basically, fix the first character at first index
    and find the rank for remaining)

Example:
Let's say out string is “VIEW”.
Character 1: 'V'
    All permutations that start with 'I', 'E' would come before 'VIEW'.
    Number of such permutations = 3! * 2 = 12
    Lets now remove ‘V’ and look at the rank of the permutation ‘IEW’.
Character 2: ‘I’
    All permutations that start with ‘E’ will come before ‘IEW’
    Number of such permutation = 2! = 2.
    Now, we will limit ourselves to the rank of ‘EW’.
Character 3:
    ‘EW’ is the first permutation when the 2 permutations are arranged.

So, we see that there are 12 + 2 = 14 permutations that would come before "VIEW".
Hence, rank of permutation = 15.
"""


class Solution:
    def findRank(self, A):
        rank = 1
        i = 0
        count = self.__smallerCharsCount(A, i)
        while i < len(A):
            rank += count * self.__fact(len(A) - 1 - i)
            i += 1
            count = self.__smallerCharsCount(A, i)
        return rank % 1000003

    def __fact(self, num):
        i = 1
        ans = 1
        while i <= num:
            ans *= i
            i += 1
        return ans

    def __smallerCharsCount(self, A, start):
        count = 0
        for i in range(start + 1, len(A)):
            if A[i] < A[start]:
                count += 1
        return count