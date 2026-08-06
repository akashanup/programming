import sys


class Solution:
    def dp(self, costs, i, a, b, lookup):
        # Base Case1: Both the cities have equal number of people. So return 0 as there ain't any people left to travel.
        if (a == len(costs) // 2) and (b == len(costs) // 2):
            return 0
        # Base Case2: If both the cities doesn't have all the people or if any city has more than half of total number of people. Return sys.maxsize as it is not a valid scenario as per the problem
        if (i == len(costs)) or (a > len(costs) // 2) or (b > len(costs) // 2):
            return sys.maxsize
        # Memoization
        key = (i, a, b)
        if key not in lookup:
            """
                Recurrence Relation:
                    A person could either travel to cityA or cityB.
                    If he travels to cityA then it's cost for cityA would be considered and the number of people in cityA would be increased by 1
                    Else he travels to cityB then it's cost for cityB would be considered and the number of people in cityB would be increased by 1
                    
                    We need to get the minimum cost by applying the above logic to all the people.
            """
            lookup[key] = min(costs[i][0] + self.dp(costs, i+1, a+1, b, lookup), costs[i][1] + self.dp(costs, i+1, a, b+1, lookup))
        return lookup[key]

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return self.dp(costs, 0, 0, 0, {})
