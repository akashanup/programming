class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    moves += 1

        moves += len(stack)
        return moves