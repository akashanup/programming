class Solution:
    def nthSuperUglyNumber(self, n, primes):
        uglyNums = [0] * n
        uglyNums[0] = 1
        nextMultiplesOfPrimes = [i for i in primes]
        primeKeys = [0] * (len(nextMultiplesOfPrimes))
        for i in range(1, n):
            uglyNums[i] = min(nextMultiplesOfPrimes)
            for key,val in enumerate(nextMultiplesOfPrimes):
                if uglyNums[i] == val:
                    primeKeys[key] += 1
                    nextMultiplesOfPrimes[key] = uglyNums[primeKeys[key]] * primes[key]
        return uglyNums[-1]
