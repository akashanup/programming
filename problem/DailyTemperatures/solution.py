class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        j = n - 2
        while j >= 0:
            if temperatures[j] < temperatures[j + 1]:
                answer[j] = 1
                j -= 1
            else:
                i = j + 1 + answer[j + 1]
                while answer[i] != 0 and temperatures[j] >= temperatures[i]:
                    i += answer[i]
                if temperatures[j] < temperatures[i]:
                    answer[j] = i - j
                else:
                    answer[j] = 0
                j -= 1
        return answer
