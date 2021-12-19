class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        labelsUsed = {}
        for label in set(labels):
            labelsUsed[label] = 0
        items = [(values[i], labels[i]) for i in range(len(values))]
        items.sort(reverse=True)
        score = 0
        for item in items:
            if numWanted == 0:
                return score
            if labelsUsed[item[1]] < useLimit:
                labelsUsed[item[1]] += 1
                score += item[0]
                numWanted -= 1
        return score
            
        
