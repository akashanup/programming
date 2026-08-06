class Solution:
    def computeMinRefills(self, distance, tank, stops):
        if distance <= tank:
            return 0
        if stops[0] > tank:
            return -1
        refill = 0
        disTravelled = tank
        stop = 1

        while stop <= len(stops):
            if stop == len(stops):
                nextMileStone = distance
            else:
                nextMileStone = stops[stop]
            if disTravelled < nextMileStone:
                # Can reach to next milestone?
                if (stops[stop - 1] + tank) >= nextMileStone:
                    disTravelled = stops[stop - 1] + tank
                    refill += 1
                else:
                    return - 1
            if disTravelled >= distance:
                return refill
            stop += 1
        return -1
