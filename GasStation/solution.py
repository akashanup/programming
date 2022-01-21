"""
    Logic:
        We will solve this problem by using the greedy approach.
        We will start from 0th station and check whether the car could complete the circle or not.
        If for the ith station the car could completes the circle then return the ith station
        Else check till where the car could go from ith station. Let's say the car could go till jth station, then
            If j is greater than i then, check for jth station whether the car could complete a circle or not (i.e, follow Step 2).
            Else, return -1 because if j is less than i then it means we could never complete a circle as we have already calculated for all stations less than i and found out that circle couldn't be completed for those stations.
"""


class Solution:
    def isCircleCompleted(self, gas, cost, station):
        amount = gas[station]
        i = 0
        while i < len(gas):
            # If the car can't move from the current station then circle can't be completed.
            if amount < cost[station]:
                return False, station
            # Next station would be reached by utilizing cost[station] gas.
            amount -= cost[station]
            # Next station in the circular route.
            station = (station+1) % len(gas)
            # Amount of gas available in the next station.
            amount += gas[station]
            i += 1
        return True, None

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station = 0
        while station < len(gas):
            if gas[station] >= cost[station]:
                circleCompleted, nextStation = self.isCircleCompleted(gas, cost, station)
                if circleCompleted:
                    return station
                if nextStation > station:
                    station = nextStation
                else:
                    return -1
            else:
                station += 1
        return -1
