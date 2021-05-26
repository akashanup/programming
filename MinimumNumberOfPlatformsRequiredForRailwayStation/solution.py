class Solution:
    def findPlatform(self, arrivals, departures):
        platforms = 1
        tempPlatforms = 1
        arrivals = sorted(arrivals)
        departures = sorted(departures)
        noOfTrains = len(arrivals)
        i = 1
        j = 0
        while i < noOfTrains and j < noOfTrains:
            if arrivals[i] <= departures[j]:
                tempPlatforms += 1
                i += 1
            elif arrivals[i] > departures[j]:
                tempPlatforms -= 1
                j += 1
        return max(platforms, tempPlatforms)
