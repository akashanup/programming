class Solution:
    def findPlatform(self, arr, dep):
        platforms = 1
        maxPlatforms = 1
        arr = sorted(arr)
        dep = sorted(dep)
        i = 1
        j = 0
        trains = len(arr)
        while i < trains and j < trains:
            if arr[i] <= dep[j]:
                platforms += 1
                i += 1
            elif arr[i] > dep[j]:
                platforms -= 1
                j += 1
            maxPlatforms = max(platforms, maxPlatforms)
        return maxPlatforms


arrival = ["09:00", "09:40", "09:50", "11:00", "15:00", "18:00"]
departure = ["09:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(Solution().findPlatform(arrival, departure)) #3
arrival = ["09:00", "09:40"]
departure = ["09:10", "12:00"]
print(Solution().findPlatform(arrival, departure)) #1
