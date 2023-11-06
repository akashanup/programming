"""
    Logic:
        We will solve this problem by using the greedy approach.
        We will start from 0th station and check whether the car could complete the circle or not.
        If for the ith station, the car could complete the circle then return to the ith station
        Else check till where the car could go from ith station. Let's say the car could go till jth station, then
            If j is greater than i then, check for jth station whether the car could complete a circle or not (i.e, follow Step 2).
            Else, return -1 because if j is less than i then it means we could never complete a circle as we have already calculated for all stations less than i and found out that circle couldn't be completed for those stations.
"""


class Solution:

    def farthestStationReached(self, gas, cost, station):
        balanceGas = 0
        gasVisited = 0
        while gasVisited < len(gas):
            balanceGas += gas[station] - cost[station]
            if balanceGas < 0:
                break
            else:
                station = (station + 1) % len(gas)
            gasVisited += 1
        return station

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station = 0
        while station < len(gas):
            if gas[station] >= cost[station]:
                farthestStation = self.farthestStationReached(gas, cost, station)
                if station == farthestStation:
                    return station
                if farthestStation > station:
                    station = farthestStation
                else:
                    return -1
            else:
                station += 1
        return -1
