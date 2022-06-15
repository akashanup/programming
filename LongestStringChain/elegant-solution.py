class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        dp = {}

        wordsList = set(words)

        for word in words:
            if word not in dp:
                maxLen = 1
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)+1):
                        newWord = word[:i] + ch + word[i:]
                        if newWord in wordsList:
                            maxLen = max(maxLen, 1+dp[newWord])
                dp[word] = maxLen
        return max(dp.values())

        
