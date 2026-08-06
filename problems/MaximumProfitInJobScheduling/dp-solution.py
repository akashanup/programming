class Solution:
    def getNextEligibleJob(self, jobs, index):
        for i in range(index+1, len(jobs)):
            if jobs[i][0] >= jobs[index][1]:
                return i
        return None

    def recur(self, jobs, currentJobIndex, lookup):
        if currentJobIndex == len(jobs):
            return 0
        key = currentJobIndex
        if key not in lookup:
            maxProfit = jobs[currentJobIndex][2]
            nextValidJobIndex = self.getNextEligibleJob(jobs, currentJobIndex)
            if nextValidJobIndex:
                maxProfit += self.recur(jobs, nextValidJobIndex, lookup)
            lookup[key] = max(maxProfit, self.recur(jobs, currentJobIndex+1, lookup))
        return lookup[key]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        return self.recur(jobs, 0, {})
