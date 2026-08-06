class Solution:
    def findMismatch(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append([s[i], i])
            elif s[i] in ")]}":
                if len(stack) and ((s[i] == ")" and stack[-1][0] == "(") or (s[i] == "]" and stack[-1][0] == "[") or (s[i] == "}" and stack[-1][0] == "{")):
                    stack.pop()
                else:
                    return i + 1
        return "Success" if not len(stack) else stack[0][1] + 1
