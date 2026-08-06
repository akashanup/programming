class Solution(object):
    def dp(self, text, pattern, t, p, lookup):
        if (t, p) not in lookup:
            # Base Case:
            # If all the characters of pattern has been verified then return:
            #   True if all characters of text has also been verified
            #   Else False
            if p == len(pattern):
                ans = t == len(text)

            else:
                isValid = t < len(text) and (pattern[p] == text[t] or pattern[p] == '.')

                if p < len(pattern)-1 and pattern[p+1] == '*':
                    # Since '*' Matches zero or more of the preceding element.
                    # Possibilities:
                    #   1. '*' is treated as a null(zero match with preceding element), so pattern[p+2] should be checked with text[t]
                    #   2. '*' is treated as a match, so now, if pattern[p] matches with text[t], the next must be pattern[p] with text[t+1] as text[t+1] might be equal to text[t] so, pattern[p] must match text[t+1]
                    ans = self.dp(text, pattern, t, p+2, lookup) or (isValid and self.dp(text, pattern, t+1, p, lookup))
                else:
                    # Else, proceed for next character if it is a valid match for current character.
                    ans = isValid and self.dp(text, pattern, t+1, p+1, lookup)
            lookup[(t, p)] = ans
        return lookup[(t, p)]

    def isMatch(self, text, pattern):
        return self.dp(text, pattern, 0, 0, {})
