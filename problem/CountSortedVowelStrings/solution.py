class Solution:
    def countVowelStrings(self, n: int) -> int:
        combinations = {'a':1, 'e': 1, 'i':1, 'o':1, 'u':1}
        for i in range(1, n):
            temp = {}
            totalCombinations = sum(combinations.values())
            temp['a'] = totalCombinations
            temp['e'] = temp['a'] - combinations['a']
            temp['i'] = temp['e'] - combinations['e']
            temp['o'] = temp['i'] - combinations['i']
            temp['u'] = temp['o'] - combinations['o']
            combinations = temp
        return sum(combinations.values())
