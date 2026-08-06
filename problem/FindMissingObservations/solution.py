class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missedSum = (mean * (len(rolls) + n)) - sum(rolls)
        """
        Minimum missedSum could be n when all the observation would be 1.
        Maximum missedSum could be 6*n when all the observation would be 6.
        Hence if missedSum is out of [n, 6*n] range then answer is not possible.
        """
        if missedSum < n or missedSum > 6 * n:
            return []
        """
        To find the missed observations list of length n, if we find the average value of missed observations values 
        and assign all of them with the missedAverageValue and then missedSumRemaining would be 
        missedSum - missedAverageValue*n.
        Now add 1 to each value of missed observations one by one from missedSumRemaining until it become 0.
        """
        missedAverageValue = missedSum // n
        missedSumRemaining = missedSum % n
        missedObservations = [missedAverageValue] * n
        for i in range(missedSumRemaining):
            missedObservations[i] += 1
        return missedObservations

