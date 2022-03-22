"""
Logic:
    Since the length of string is fixed and we have to make the lexicographically smallest string so our intention should be putting the largest alphabet at end and smallest alphabet at the beginning.
    This can be achieved if we start building our string from end and try to place the largest alphabet possible.
    Now the question arises as which alphabet would be the largest alphabet for a particular index.
    Let us start building the string from end-
        If for any index i if we can assure that if we place z at that index and remaining indexes could be filled having sum k-26 then simply place z at that index.
        Else, place the largest possible alphabet at that index. Largest possible alphabet can be calculated by considering the remaining indexes are all filled with as i.e., chr(96+ k -(i-1)).
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        string = []
        for i in range(n,0,-1):
            if k - (i - 1) >= 26:
                k -= 26
                string.append('z')
            else:
                string.append(chr(96 + k - (i - 1)))
                k = i - 1
        return ''.join(string[::-1])
