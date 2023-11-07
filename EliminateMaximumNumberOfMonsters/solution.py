class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Time taken by monsters' to reach the city.
        monsterTimes = [ceil(dist[i] / speed[i]) for i in range(len(dist))]
        monsterTimes.sort()
        # Time elapsed (Also tells the number of monsters eliminated)
        timeElapsed = 0
        for monsterTime in monsterTimes:
            # Monster entered the city
            if monsterTime - timeElapsed <= 0:
                break
            timeElapsed += 1
        return timeElapsed
