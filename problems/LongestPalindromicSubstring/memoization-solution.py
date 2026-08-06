class Solution:

    def __init__(self):
        self.maxPalindromeSize = 0
        self.ans = ""

    def dp(self, s, i, j, lookup):
        if i > j:
            return True

        key = (i, j)
        if i == j:
            lookup[key] = True
        elif key not in lookup:
            if s[i] == s[j] and self.dp(s, i+1, j-1, lookup):
                lookup[key] = True
                if j-i+1 > self.maxPalindromeSize:
                    self.maxPalindromeSize = j-i+1
                    self.ans = s[i:j+1]
            else:
                lookup[key] = False
                self.dp(s, i+1, j, lookup)
                self.dp(s, i, j-1, lookup)
        return lookup[key]

    def longestPalindrome(self, s: str) -> str:
        self.dp(s, 0, len(s)-1, {})
        return self.ans


print(Solution().longestPalindrome("babad"))
