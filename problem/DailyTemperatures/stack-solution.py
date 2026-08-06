class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for key, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                answer[j] = key - j
            stack.append(key)
        return answer
