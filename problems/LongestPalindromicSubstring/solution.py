import heapq


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        heap = []
        heapq.heapify(heap)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    heapq.heappush(heap, [(-1 * (abs(i-j) + 1)), s[i:j+1]])

        return heapq.heappop(heap)[1]


print(Solution().longestPalindrome("abcdcbaabcd"))
