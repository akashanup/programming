class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1=Counter(word1)
        counter2=Counter(word2)
        key1=set(counter1.keys())
        key2=set(counter2.keys())
        val1=list(counter1.values())
        val2=list(counter2.values())
        val1.sort()
        val2.sort()
        return key1==key2 and val1==val2
