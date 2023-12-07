class Solution:
    def findPlatform(self, arr, dep):
        trains = [[_, "A"] for _ in arr] + [[_, "D"] for _ in dep]
        trains.sort()
        platforms = 0
        maxPlatforms = 0
        for train in trains:
            if train[1] == "A":
                platforms += 1
            else:
                platforms -= 1
            maxPlatforms = max(maxPlatforms, platforms)
        return maxPlatforms


arrival = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departure = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(Solution().findPlatform(arrival, departure))  # 3
arrival = ["09:00", "09:40"]
departure = ["09:10", "12:00"]
print(Solution().findPlatform(arrival, departure))  # 1
