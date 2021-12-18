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
            # Start time of current job as every job takes a unit amount of time.
            deadline = job[1] - 1
            # Check if any slot is available before the deadline of current job
            while deadline >= 0 and deadlines[deadline] is not True:
                deadline -= 1
            # If a vacant slot is found then assign the current job to that slot and count it profit.
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
