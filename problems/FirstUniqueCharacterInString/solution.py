class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = {}
        for i in s:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        for index, i in enumerate(s):
            if lookup[i] == 1:
                return index
        return -1
