class Solution:
    def isPalindrome(self, s, lookup):
        # Check from previous computed results to optimize the checking.
        if s not in lookup:
            start, end = 0, len(s)-1
            palindrome = True
            while start < end:
                if s[start] != s[end]:
                    lookup[s[start:end+1]] = 0
                    palindrome = False
                    break
                elif s[start:end+1] in lookup:
                    palindrome = bool(lookup[s[start:end+1]])
                    break
                start += 1
                end -= 1
            lookup[s] = int(palindrome)
        return lookup[s]

    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        lookup = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                palindromes += self.isPalindrome(s[i:j+1], lookup)

        return palindromes
