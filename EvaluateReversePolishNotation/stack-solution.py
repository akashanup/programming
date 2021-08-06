class Solution:
    def performOperation(self, num1, num2, operator):
        if operator == '+':
            return num2 + num1
        elif operator == '-':
            return num2 - num1
        elif operator == '/':
            return int(num2 / num1)
        elif operator == '*':
            return num2 * num1

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for token in tokens:
            if token in ['+', '-', '/', '*']:
                stack.append(self.performOperation(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack.pop()

