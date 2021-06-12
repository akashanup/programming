class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        lookup = [startFuel] + [0] * len(stations)
        for i, station in enumerate(stations):
            for j in range(i, -1, -1):
                if lookup[j] >= station[0]:
                    lookup[j + 1] = max(lookup[j + 1], lookup[j] + station[1])

        for stop, distance in enumerate(lookup):
            if distance >= target:
                return stop
        return -1
