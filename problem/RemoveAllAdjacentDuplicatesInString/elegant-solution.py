class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack.pop()
            else:
                stack.append([ch, 1])

        return ''.join([ch for ch, _ in stack])
