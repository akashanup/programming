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
