class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        '''
            Store the index and height of bar and sort it in decreasing order.
            Now there will be a enclosed area/portion between lookup[i][0] and lookup[i+1][0] where water can be stored
            We need to just calculate the amount of water stored in each slot distinctly.
            Now, the amount of water for each portion would be calculated as-
            1. Get the max and second max Height of the portion.
            2. Iterate for each index and the amount of water at that index(say i) would be the (second max height of that portion - height[i])  
        '''
        lookup = [[i, height[i]] for i in range(len(height)) if height[i] > 0]
        lookup.sort(key=lambda x: x[1], reverse=True)
        # covered will have two pointers, start and end which means that at any point of time, the amount of water between start and end is already calculated.
        covered = []
        # Iterate over each slot.
        for i in range(len(lookup) - 1):
            if covered:
                '''
                    If the index of bar with next highest height is greater than the end index of which the amount of water is calculated then,
                    Calculate the amount of water from end to the index of next highest height of bar and update the end pointer.
                '''
                if covered[1] <= lookup[i + 1][0]:
                    for j in range(covered[1] + 1, lookup[i + 1][0]):
                        water += (lookup[i + 1][1] - height[j])
                    covered[1] = lookup[i + 1][0]
                '''
                    If the start pointer is greater than the index of bar with next highest height then,
                    Calculate the amount of water from the index of next highest height of bar to start pointer and update the start pointer.
                '''
                if covered[0] > lookup[i][0]:
                    for j in range(lookup[i][0], covered[0]):
                        water += (lookup[i][1] - height[j])
                    covered[0] = lookup[i][0]
                if covered[0] > lookup[i + 1][0]:
                    for j in range(lookup[i + 1][0], covered[0]):
                        water += (lookup[i + 1][1] - height[j])
                    covered[0] = lookup[i + 1][0]
            else:
                # covered[0] means the start index and covered[1] means the end index of which the stored amount of water is calculated.
                covered = [min(lookup[i][0], lookup[i + 1][0]), max(lookup[i][0], lookup[i + 1][0])]
                for j in range(covered[0] + 1, covered[1]):
                    water += (lookup[i + 1][1] - height[j])
        return water
