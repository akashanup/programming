class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        # Loop through all the char of s
        for i in range(len(s)):
            # If the char is not encountered yet then...
            if s[i] not in lookup:
                # If the replacable value of the char is not already used to replace any other char then add it to lookup.
                if t[i] not in lookup.values():
                    lookup[s[i]] = t[i]
                # If the replacable value of the char is used to replace any other char then the strings are not isomorphic
                else:
                    return False
            # If the char is already encountered but its replacable value doesn't match with the value in lookup then the strings are not isomorphic
            elif lookup[s[i]] != t[i]:
                return False
        return True
