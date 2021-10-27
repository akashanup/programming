class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)

        if s2len < s1len:
            return False

        hashmapS1 = [0] * 26
        hashmapS2 = [0] * 26

        for ch in s1:
            hashmapS1[ord(ch)-ord('a')] += 1

        left = 0
        right = s1len - 1

        for ch in range(left, right+1):
            hashmapS2[ord(s2[ch])-ord('a')] += 1

        while right < s2len:
            if hashmapS1 == hashmapS2:
                return True
            hashmapS2[ord(s2[left])-ord('a')] -= 1
            left += 1
            right += 1
            if right < s2len:
                hashmapS2[ord(s2[right])-ord('a')] += 1
        return False
