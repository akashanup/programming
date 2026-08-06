class Solution:
    def maxActivities(self, activities):
        # Sort activities by finish time.
        activities.sort(key=lambda x: x[1])
        # At least once activity would definitely be performed.
        maxActivitiesCount = 1
        j = 0
        for i in range(1, len(activities)):
            if activities[i][0] >= activities[j][1]:
                maxActivitiesCount += 1
                j = i
        return maxActivitiesCount
