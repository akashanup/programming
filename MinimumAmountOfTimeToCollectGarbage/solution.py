class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        timeTaken = 0
        garbageTypes = {"M": {}, "P": {}, "G": {}}
        travelTime = [0] * len(garbage)
        for house in range(1, len(garbage)):
            travelTime[house] = travelTime[house - 1] + travel[house - 1]

        for house, garbages in enumerate(garbage):
            for garbageType in garbages:
                if house not in garbageTypes[garbageType]:
                    garbageTypes[garbageType][house] = 0
                garbageTypes[garbageType][house] += 1

        for garbageType, houses in garbageTypes.items():
            # House, at which the garbageType truck was previously visited.
            prevHouse = 0
            for house in range(len(garbage)):
                if house in houses:
                    # Time taken to reach the current house from previous house
                    timeTaken += travelTime[house] - travelTime[prevHouse]
                    # Time taken to collect all the current garbage type from the current house
                    timeTaken += houses[house]
                    prevHouse = house

        return timeTaken
