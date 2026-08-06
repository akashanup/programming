class Solution:
    def findIntegers(self, n: int) -> int:
        binN = bin(n + 1)[2:]
        binNLen = len(binN)
        # integersCount[i] is the total number of integers till (2**i - 1) which fulfills the requirements given in the question.
        integersCount = [1, 2]
        i = 2
        while i < binNLen:
            integersCount.append(integersCount[i - 1] + integersCount[i - 2])
            i += 1
        # Till now we know the total number of integers < (2 ** indices) - 1 which fulfills the requirements given in the question.
        totalIntegers = 0
        for i in range(binNLen):
            if binN[i] != "0":
                # if bit is 1 then add the total count from integersCount from right end
                totalIntegers += integersCount[-(i+1)]
                # if consecutive 1s are found then that could be the max number of integers fulfilling the reuirements till n.
                if i > 0 and binN[i - 1] == "1":
                    break
        return totalIntegers
