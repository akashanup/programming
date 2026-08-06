class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashmap = {}
        for i, ch in enumerate(s):
            if ch not in hashmap:
                hashmap[ch] = [i, None]
            hashmap[ch][-1] = i

        uniquePalindromesCount = 0
        for ch in hashmap.keys():
            start, end = hashmap[ch]
            if end:
                palindromes = set()
                for mid in range(start + 1, end):
                    palindromes.add((ch, s[mid], ch))
                uniquePalindromesCount += len(palindromes)
        return uniquePalindromesCount
