class Solution:
    def dp(self, s1, s2, s, lookup):
        # If all the three strings are exhausted then we have found the Interleaving String.
        if not s1 and not s2 and not s:
            return True
        # If at any point the sum of lengths of s1 and s2 doesn't equl to the length of s then we can't find Interleaving String.
        if len(s1) + len(s2) != len(s):
            return False

        key = (s, s1, s2)
        if key not in lookup:
            a, b = False, False
            # If the characters at first index of s1 and s matches then check for the remaining characters.
            if s1 and s1[0] == s[0]:
                a = self.dp(s1[1:], s2, s[1:], lookup)
            # If the characters at first index of s2 and s matches then check for the remaining characters.
            if s2 and s2[0] == s[0]:
                b = self.dp(s1, s2[1:], s[1:], lookup)
            # If either of the above scenarios yeilds True then we have Interleaving String.
            lookup[key] = a or b
        return lookup[key]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.dp(s1, s2, s3, {})
