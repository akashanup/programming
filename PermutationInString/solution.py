class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)

        if s2len < s1len:
            return False

        hashmapS1 = [0] * 26
        hashmapS2 = [0] * 26

        # Generate hashmap for s1
        for ch in s1:
            hashmapS1[ord(ch)-ord('a')] += 1

        # Generate hashmap for the first window of length len(s1) for s2
        for i in range(len(s1)):
            hashmapS2[ord(s2[i])-ord('a')] += 1

        start = 0
        end = len(s1) - 1
        # Start comparing hashmapS1 with hashmapS2 for all the windows until a match is found.
        while end < len(s2):
            if hashmapS1 == hashmapS2:
                return True
            # Move to next window and update the hashmapS2 for that start and end.
            hashmapS2[ord(s2[start]) - ord('a')] -= 1
            start += 1
            end += 1
            if end < len(s2):
                hashmapS2[ord(s2[end]) - ord('a')] += 1
        return False
