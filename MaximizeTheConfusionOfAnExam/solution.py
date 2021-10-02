class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxTrue = 0
        start = 0
        falseCount = 0
        for end in range(len(answerKey)):
            if answerKey[end] == 'F':
                falseCount += 1
            while falseCount > k:
                if answerKey[start] == 'F':
                    falseCount -= 1
                start += 1
            maxTrue = max(maxTrue, end - start + 1)

        maxFalse = 0
        start = 0
        trueCount = 0
        for end in range(len(answerKey)):
            if answerKey[end] == 'T':
                trueCount += 1
            while trueCount > k:
                if answerKey[start] == 'T':
                    trueCount -= 1
                start += 1
            maxFalse = max(maxFalse, end - start + 1)

        return max(maxFalse, maxTrue)
