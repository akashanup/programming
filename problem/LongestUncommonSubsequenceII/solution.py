class Solution:
    def getSubsequences(self, s, subsequences, subsequence, index):
        if subsequence:
            subsequences.append(subsequence)
        for i in range(index, len(s)):
            subsequence += s[i]
            self.getSubsequences(s, subsequences, subsequence, i+1)
            subsequence = subsequence[:-1]
        return subsequences

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda x: len(x), reverse=True)
        i = 0
        subsequences = []
        while i < len(strs):
            j = 0
            found = False
            while j < len(strs):
                if i != j and strs[i] in strs[j]:
                    found = True
                    break
                j += 1
            if not found and strs[i] not in subsequences:
                return len(strs[i])
            if strs[i] not in strs[:i]:
                subsequences += self.getSubsequences(strs[i], [], '', 0)
            i += 1
        return -1
