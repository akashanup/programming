class Solution:
    def getMaxDeadline(self, jobs):
        maxDeadLine = 0
        for job in jobs:
            maxDeadLine = max(maxDeadLine, job[1])
        return maxDeadLine

    def jobScheduling(self, jobs, n):
        maxDeadLine = self.getMaxDeadline(jobs)
        deadlines = [True for _ in range(maxDeadLine)]
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxProfit = 0
        for job in jobs:
            deadline = job[1] - 1
            while deadline >= 0 and deadlines[deadline] is not True:
                deadline -= 1
            if deadline >= 0 and deadlines[deadline] is True:
                deadlines[deadline] = False
                maxProfit += job[2]

        return maxProfit


jobs = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15],
        ]
print(Solution().jobScheduling(jobs, 5))
