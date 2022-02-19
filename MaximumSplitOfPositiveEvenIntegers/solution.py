"""
Logic:
    Since we want the split array to be of maximum length so, a very straight forward solution would be to generate the array from the minimum even number(i.e, 2) and keep adding the next even number until the finalSum is reached.
    If finalSum is exactly reached i.e, the finalSum minus sum of split array is zero, then split array is our answer.
    Else just add the remaining(finalSum - sum(splitArray)) to the last element of the split array and that would be our answer.
"""


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        evenSplit = []
        evenNum = 2
        while evenNum <= finalSum:
            evenSplit.append(evenNum)
            finalSum -= evenNum
            evenNum += 2
        # Add the remaining to the last element of array.
        evenSplit[-1] += finalSum
        return evenSplit
