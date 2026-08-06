class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = {}
        for str in sorted(strs):
            sortedStr = tuple(sorted(str))
            if sortedStr in lookup:
                lookup[sortedStr].append(str)
            else:
                lookup[sortedStr] = [str]
        return list(lookup.values())
