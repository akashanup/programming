class Solution:
    def countHomogenous(self, s: str) -> int:
        lastChar = None
        lastCharCount = 0
        substrings = 0
        for ch in s:
            if ch == lastChar:
                lastCharCount += 1
            else:
                # Number of substrings of a string of length n is (n*(n+1))/2
                substrings += (lastCharCount * (lastCharCount+1) // 2)
                lastChar = ch
                lastCharCount = 1
        # Number of substrings of a string of length n is (n*(n+1))/2
        substrings += (lastCharCount * (lastCharCount+1) // 2)
        return substrings % ((10**9)+7)

