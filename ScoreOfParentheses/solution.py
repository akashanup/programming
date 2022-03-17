class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == ')':
                # If ch is ')' then calculate the score till previous '(' as per the formula and append the score into stack.
                score = 0
                while stack and stack[-1] != '(':
                    score += stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
                stack.append(2 * score if score > 0 else 1)
            else:
                # If ch is '(' then simple put it into stack
                stack.append(ch)
        return sum(stack)
