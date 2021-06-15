class Solution:
    def dpFn(self, matchsticks, n, sideLength, sides, i, lookup):
        key = tuple(sorted(sides))
        if key not in lookup:
            if i == n:
                lookup[key] = sides[0] == sides[1] == sides[2] == sides[3] == sideLength
            else:
                for s in range(4):
                    if sides[s] + matchsticks[i] <= sideLength:
                        sides[s] = sides[s] + matchsticks[i]
                        if self.dpFn(matchsticks, n, sideLength, sides, i + 1, lookup):
                            lookup[key] = True
                            break
                        sides[s] = sides[s] - matchsticks[i]
                if key not in lookup:
                    lookup[key] = False
        return lookup[key]

    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4:
            return False
        sideLength = perimeter // 4
        matchsticks = sorted(matchsticks, reverse=True)
        if matchsticks[0] > sideLength:
            return False
        return self.dpFn(matchsticks, len(matchsticks), sideLength, [0, 0, 0, 0], 0, {})
