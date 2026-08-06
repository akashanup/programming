import sys


class Solution:
    def dp(self, jobDifficulty, n, d, mostDifficultJobs, currentJob, currentDay, lookup):
        # Base case, it's the last day, so we need to finish all the jobs
        if d == currentDay:
            return mostDifficultJobs[currentJob]
        """
            To adhere that at least one job must be performed at each day then the maximum number of jobs that can be performed on ith day would be total number of jobs - total number of already performed jobs - remaining number of days.
            Now we need to know which set of sequential jobs can be performed on the current day which will lead to minimum difficulty job scheduling so we will check all the possible set of sequential jobs and determine the minimum difficulty job scheduling.
        """
        if lookup[currentJob][currentDay] == -1:
            mostDifficultJob = 0
            minDifficultyJobSchedule = sys.maxsize
            for i in range(currentJob, n - (d - currentDay)):
                mostDifficultJob = max(mostDifficultJob, jobDifficulty[i])
                minDifficultyJobSchedule = min(minDifficultyJobSchedule,
                                               mostDifficultJob + self.dp(jobDifficulty, n, d, mostDifficultJobs, i + 1,
                                                                          currentDay + 1, lookup))
            lookup[currentJob][currentDay] = minDifficultyJobSchedule
        return lookup[currentJob][currentDay]

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # At least one job must be performed on each day so if the number of jobs is less than number of days then it is impossible.
        if n < d:
            return -1

        # Precompute the most difficult job in case of all the further jobs including the current job are done on same day.
        mostDifficultJobs = [0] * n
        mostDifficultJob = 0
        for currentJobIndex in range(n - 1, -1, -1):
            mostDifficultJob = max(mostDifficultJob, jobDifficulty[currentJobIndex])
            mostDifficultJobs[currentJobIndex] = mostDifficultJob

        return self.dp(jobDifficulty, n, d, mostDifficultJobs, 0, 1, [[-1 for _ in range(d)] for _ in range(n)])
