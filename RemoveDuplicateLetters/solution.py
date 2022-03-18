class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Store last index of each char which will help to determine whether the char has a duplicate or not.
        lastIndex = {}
        for index, ch in enumerate(s):
            lastIndex[ch] = index
        stack = []
        for index, ch in enumerate(s):
            # Check while top of stack occurs further also and is greater than ch then pop it and push ch
            if ch not in stack:
                while stack and stack[-1] > ch and lastIndex[stack[-1]] > index:
                    stack.pop()
                stack.append(ch)
        return ''.join(stack)
