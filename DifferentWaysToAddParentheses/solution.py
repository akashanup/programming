class Solution:
    def __combinations(self, i, j, expression):
        res = []
        # Base case
        if j - i + 1 <= 2:
            res.append(int(expression[i:j + 1]))
            return res

        for idx in range(i, j + 1):
            if expression[idx] in ("+", "-", "*"):
                op = expression[idx]

                # Get all results for its left and right substring using recursion
                left = self.__combinations(i, idx - 1, expression)
                right = self.__combinations(idx + 1, j, expression)

                # Evaluate all options for left & right operands and push all results to the answer
                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l + r)
                        elif op == '-':
                            res.append(l - r)
                        elif op == '*':
                            res.append(l * r)
        return res

    def diffWaysToCompute(self, expression: str):
        return self.__combinations(0, len(expression) - 1, expression)