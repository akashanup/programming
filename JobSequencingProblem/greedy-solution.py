class Solution:
    def getMaxDeadline(self, jobs):
        maxDeadLine = 0
        for job in jobs:
            maxDeadLine = max(maxDeadLine, job[1])
        return maxDeadLine

    def jobScheduling(self, jobs, n):
        # Find the maximum deadline among all the jobs
        maxDeadLine = self.getMaxDeadline(jobs)
        # Make an array of deadlines from 0 to maxDeadline denoting the deadline slots.
        deadlines = [True for _ in range(maxDeadLine)]
        # Sort the jobs based on profit in decreasing order to always accommodate those jobs which has more profit.
        jobs.sort(key=lambda x: x[2], reverse=True)
        maxProfit = 0
        for job in jobs:
            # Last slot of any job could be (deadline - 1) as every job takes a unit amount of time.
            lastSlot = job[1] - 1
            # Check if any slot is available before the last slot of current job
            while lastSlot >= 0 and deadlines[lastSlot] is not True:
                lastSlot -= 1
            # If a vacant slot is found then assign the current job to that slot and count its profit.
            if lastSlot >= 0 and deadlines[lastSlot] is True:
                deadlines[lastSlot] = False
                maxProfit += job[2]

        return maxProfit


jobs = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15],
        ]
print(Solution().jobScheduling(jobs, 5))
