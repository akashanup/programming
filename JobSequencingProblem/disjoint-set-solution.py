class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def findParent(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.findParent(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        self.parent[j] = i


class Solution:
    def getMaxDeadline(self, jobs):
        maxDeadLine = 0
        for job in jobs:
            maxDeadLine = max(maxDeadLine, job[1])
        return maxDeadLine

    def jobScheduling(self, jobs, n):
        maxDeadLine = self.getMaxDeadline(jobs)
        disjointSet = DisjointSet(maxDeadLine)
        jobs.sort(key=lambda x: x[2], reverse=True)
        print(jobs)
        maxProfit = 0
        for job in jobs:
            availableSlot = disjointSet.findParent(job[1])
            print(job, availableSlot)
            print(disjointSet.parent)
            if availableSlot > 0:
                disjointSet.union(availableSlot - 1, availableSlot)
                maxProfit += job[2]
            print(disjointSet.parent)
        return maxProfit


jobs = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15],
        ]
print(Solution().jobScheduling(jobs, 5))
