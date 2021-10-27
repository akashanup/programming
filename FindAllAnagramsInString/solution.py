class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS = len(s)
        lenP = len(p)

        if lenS < lenP:
            return []

        hashmapS = [0] * 26
        hashmapP = [0] * 26

        for ch in p:
            hashmapP[ord(ch) - ord('a')] += 1

        left = 0
        right = lenP - 1

        for ch in range(left, right+1):
            hashmapS[ord(s[ch]) - ord('a')] += 1

        output = []

        while right < lenS:
            if hashmapP == hashmapS:
                output.append(left)
            hashmapS[ord(s[left]) - ord('a')] -= 1
            left += 1
            right += 1
            if right < lenS:
                hashmapS[ord(s[right]) - ord('a')] += 1
        if hashmapP == hashmapS:
            output.append(left)

        return output

