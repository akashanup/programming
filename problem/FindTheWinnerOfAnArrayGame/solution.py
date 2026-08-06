class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        maxElement = max(arr)
        if maxElement == arr[0] or k >= len(arr):
            return maxElement

        winCount = 0
        lastRoundWinnerIndex = 0
        currentElementIndex = 1
        while winCount != k and arr[lastRoundWinnerIndex] != maxElement:
            currentRoundWinnerIndex = -1
            if arr[currentElementIndex] > arr[lastRoundWinnerIndex]:
                currentRoundWinnerIndex = currentElementIndex
            else:
                currentRoundWinnerIndex = lastRoundWinnerIndex

            if currentRoundWinnerIndex == lastRoundWinnerIndex:
                winCount += 1
            else:
                winCount = 1
            lastRoundWinnerIndex = currentRoundWinnerIndex
            currentElementIndex += 1
        return arr[lastRoundWinnerIndex]
