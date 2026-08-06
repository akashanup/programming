"""
Logic:
    This problem can be tackeled by using Rabin-Karp Algorithm. Before going further I would suggest to go to this algorithm first.
    The only modification required in the above algorithm is in hashing function.
    In Rabin-Karp, the index of power variable starts from k-1 and ends to 0 and in this problem, the index of power variable starts from 0 and ends to k-1. Rest remains the same.
"""


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        p = 0
        mul = 1
        
        # Calculate the hash value for first window of length k of s.
        for i in range(k):
            p += (ord(s[i])-ord('a')+1) * mul
            mul *= power
        mul //= power
        
        # Slide the pattern over text one by one.
        for j in range(len(s)-k+1):
            # Iff hash value of current window of s matches with given hashValue then we have our answer.
            if p%modulo == hashValue:
                return s[j:j+k]
            if j < len(s)-k:
                p = ((p - (ord(s[j])-ord('a')+1)) // power) + ((ord(s[j+k])-ord('a')+1) * mul)
