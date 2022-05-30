class Solution:

    def longestSubsequence(self, source, target, targetIdx):
        targetStartIdx = targetIdx
        sourceIdx = 0
        while sourceIdx < len(source) and targetIdx < len(target):
            if source[sourceIdx] == target[targetIdx]:
                targetIdx += 1
            sourceIdx += 1
        if targetIdx == targetStartIdx:
            return -1
        return targetIdx

    def shortestWay(self, source: str, target: str) -> int:
        steps = 0
        targetIdx = 0
        while targetIdx < len(target):
            targetIdx = self.longestSubsequence(source, target, targetIdx)
            if targetIdx < 0:
                return -1
            steps += 1
        return steps


print(Solution().shortestWay(source="abc", target="abcbc"))
print(Solution().shortestWay(source="abc", target="acdbc"))
print(Solution().shortestWay(source="xyz", target="xzyxz"))
