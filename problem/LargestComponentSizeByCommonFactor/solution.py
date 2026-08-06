"""
Let us consider example [2,3,6,7,4,12,21,39] an go through the code:

1. getPrimesFactors(self,n) return set of unique prime divisors of number n, for example for n = 12 it returns set [2,3] and for n=39 it returns set [3,13].
2. For each found prime, we put indexes of numbers from nums, which are divisible by this prime. For our example we have: 2: [0,2,4,5], 3:[1,2,5,6,7], 7:[3,6], 13:[7]. So, what we need to do now? We need to union 0-2-4-5, 1-2-5-6-7 and 3-6.
3. That exactly what we do on the next step: iterate over our primes and create connections with union(indexes[i], indexes[i+1])
4. Finally, when we made all connections, we need to find the biggest group: so we find parent for each number and find the biggest frequency.
"""
import math


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for vertex in range(len(vertices)):
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[y] > self.rank[x]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += 1
        
        
class Solution:
    def getPrimesFactors(self, num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return self.getPrimesFactors(num//i) | {i}
        return {num}

    def largestComponentSize(self, nums: List[int]) -> int:
        primeFactors = {}
        for index, num in enumerate(nums):
            for prime in self.getPrimesFactors(num):
                if prime in primeFactors:
                    primeFactors[prime].append(index)
                else:
                    primeFactors[prime] = [index]

        djs = DisjointSet(nums)
        for indexes in primeFactors.values():
            for index in range(len(indexes) - 1):
                djs.union(indexes[index], indexes[index + 1])

        longestConnectedComponentLength = 1
        components = {}
        for index in range(len(nums)):
            x = djs.find(index)
            if x in components:
                components[x] += 1
                longestConnectedComponentLength = max(longestConnectedComponentLength, components[x])
            else:
                components[x] = 1

        return longestConnectedComponentLength
