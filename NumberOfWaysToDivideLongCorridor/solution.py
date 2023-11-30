class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seatsCount = corridor.count("S")
        # If seats count is odd then the corridor can't be divided with having exactly two seats in each section.
        if seatsCount == 0 or seatsCount % 2 != 0:
            return 0
        if seatsCount == 2:
            return 1
        # Store the start and end of each seat pairs.
        seatsPositionsInPair = [[None, None]]
        for idx, ch in enumerate(corridor):
            if ch == "S":
                if seatsPositionsInPair[-1][0] is None:
                    seatsPositionsInPair[-1][0] = idx
                elif seatsPositionsInPair[-1][-1] is None:
                    seatsPositionsInPair[-1][-1] = idx
                else:
                    seatsPositionsInPair.append([idx, None])

        # Number of ways would be equal to the product of all the plants in between all the pairs.
        ways = 1
        pair = 0
        while pair < len(seatsPositionsInPair) - 1:
            ways *= seatsPositionsInPair[pair + 1][0] - seatsPositionsInPair[pair][-1]
            pair += 1
        return ways % ((10 ** 9) + 7)
