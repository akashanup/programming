class Solution:
    def getFibonacciModM(self, n, m):
        prevMod = 0
        currMod = 1
        fibModM = [0, 1]
        while True:
            prevMod, currMod = currMod % m, (prevMod + currMod) % m
            fibModM.append(currMod)
            if prevMod == 0 and currMod == 1:
                # Pisano cycle found
                pisanoCycleLength = len(fibModM) - 2
                return fibModM[n % pisanoCycleLength]
