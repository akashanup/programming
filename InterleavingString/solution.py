class Solution:
    def dpFn(self, s1, s2, s, dp):
        # Return true if the end of all strings is reached
        if not s1 and not s2 and not s:
            return True
        # Return false if the end of string `s` is reached, but `s1` or `s2` is not empty
        if not s:
            return False
        key = (s1, s2, s)
        if key not in dp:
            # If string s1 is not empty and its first character matches with the first character of s, recur for the remaining substring
            a = (len(s1) and s[0] == s1[0]) and self.dpFn(s1[1:], s2, s[1:], dp)
            # If string s2 is not empty and its first character matches with the first character of s, recur for the remaining substring
            b = (len(s2) and s[0] == s2[0]) and self.dpFn(s1, s2[1:], s[1:], dp)
            dp[key] = a or b
        return dp[key]

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) == len(s3):
            return self.dpFn(s1, s2, s3, {})
        else:
            return False
