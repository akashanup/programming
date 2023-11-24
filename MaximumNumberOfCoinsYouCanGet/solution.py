class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        myCoins = 0
        piles.sort()
        alice, me, bob = len(piles)-1, len(piles)-2, 0
        while bob < me:
            myCoins += piles[me]
            alice -= 2
            me -= 2
            bob += 1
        return myCoins

