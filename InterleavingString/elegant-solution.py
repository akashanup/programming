class Solution:
    def dp(self, s1, s2, s3, i, j, lookup):
        # If both s1 and s2 are used then we have found the Interleaving String.
        if i == len(s1) and j == len(s2):
            return True
        if (i, j) not in lookup:
            ans = False
            # If the characters at ith index of s1 and (i+j)th index of s matches then check for the remaining characters.
            if i < len(s1) and s1[i] == s3[i + j]:
                ans |= self.dp(s1, s2, s3, i + 1, j, lookup)
            # If the characters at jth index of s2 and (i+j)th index of s matches then check for the remaining characters.
            if j < len(s2) and s2[j] == s3[i + j]:
                ans |= self.dp(s1, s2, s3, i, j + 1, lookup)
            # If either of the above scenarios yields True then we have Interleaving String.
            lookup[(i, j)] = ans
        return lookup[(i, j)]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        return self.dp(s1, s2, s3, 0, 0, {})
