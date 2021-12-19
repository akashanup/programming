class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        lenS = len(s)
        i = 0
        while i < lenS:
            if s[i] == ']':
                decoded = ''
                while stack and stack[-1] != '[':
                    decoded = stack.pop() + decoded
                stack.pop()
                decoded *= int(stack.pop())
                stack.append(decoded)
            elif s[i].isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1
        decoded = ''
        while stack:
            decoded = stack.pop() + decoded
        return decoded



