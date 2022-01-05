class Solution:
    def recur(self, palindromes, s):
        # If the input string is empty then return the list of palindromes found.
        if not s:
            return [palindromes]
        output = []
        for i in range(1, len(s)+1):
            """
                Partition the input string by ith index and check whether the partitioned string is a palindrome or not.
                If yes then add the partitioned string into palindrome list and recur for finding the palindromes in partitioned string.
            """
            if s[:i] == s[:i][::-1]:
                output += self.recur(palindromes+[s[:i]], s[i:])
        return output

    def partition(self, s: str) -> List[List[str]]:
        return self.recur([], s)
