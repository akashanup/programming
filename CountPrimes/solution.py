class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        # Sieve of Eratosthenes
        primes = [True]*n
        primes[0] = False
        primes[1] = False
        i = 2
        while i*i < n:
            if primes[i]:
                j = 2
                while i*j < n:
                    primes[i*j] = False
                    j += 1
            i += 1
        return sum(primes)
                
        