class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 1:
            return s
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i] == stack[-1][0]:
                stack.append((s[i], stack[-1][1]+1))
                if stack[-1][1] == k:
                    for j in range(k):
                        stack.pop()
            else:
                stack.append((s[i], 1))
            i += 1
        return ''.join([ch for ch, _ in stack])
