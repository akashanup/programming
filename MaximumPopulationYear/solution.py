class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        lookup = {}
        for i in logs:
            for j in range(i[0],i[1]):
                if j in lookup:
                    lookup[j] += 1
                else:
                    lookup[j] = 1
                    
        lookup = dict(sorted(lookup.items()))
        return max(lookup, key = lookup.get)