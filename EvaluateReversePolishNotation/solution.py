class Solution:
    def performOperation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '/':
            return int(num1 / num2)
        elif operator == '*':
            return num1 * num2

    def calcRPM(self, tokens):
        if '+' in tokens or '-' in tokens or '/' in tokens or '*' in tokens:
            for i in range(len(tokens)):
                if tokens[i] in ['+', '-', '*', '/']:
                    operation = self.performOperation(int(tokens[i - 2]), int(tokens[i - 1]), tokens[i])
                    tokens[i - 2] = operation
                    tokens.pop(i - 1)
                    tokens.pop(i - 1)
                    tokens = self.calcRPM(tokens)
                    return tokens
        return tokens

    def evalRPN(self, tokens: List[str]) -> int:
        return self.calcRPM(tokens)[0]
