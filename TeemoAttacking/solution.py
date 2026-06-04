"""
# Intuition

Each attack poisons Ashe for `duration` seconds.
If the next attack happens before the current poison effect ends, the poison intervals overlap and some seconds get counted twice.
The idea is:
- Add the full `duration` for every attack.
- If there is an overlap with the previous poison interval, subtract the overlapping portion.

We keep track of:
- `lastPoisonedAt` → the start time of the previous attack.
- `poisonedDuration` → total poisoned time accumulated so far.

For every new attack:
- Check whether the previous poison is still active.
- If yes, subtract the overlapping duration.
- Then add the full duration for the current attack.

# Approach
1. Initialize:
    - `lastPoisonedAt` as negative infinity.
    - `poisonedDuration` as 0.
2. Traverse through each attack time t in timeSeries.
3. Check if the current attack overlaps with the previous poison interval:
    - `if t < lastPoisonedAt + duration`. This means the previous poison effect has not ended yet.
4. Compute overlap:
    - `lastPoisonedAt + duration - t`. 
    - and subtract it from the total because those seconds would otherwise be counted twice.
5. Add the full duration for the current attack.
6. Update `lastPoisonedAt` to the current attack time.
7. Return the final accumulated poisoned duration.
 

# Complexity
- Time complexity: $$O(n)$$. We iterate through the array once.
- Space complexity: $$O(1)$$. Only constant extra space is used.
"""

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        lastPoisonedAt = float('-inf')
        poisonedDuration = 0
        for t in timeSeries:
            if t < lastPoisonedAt + duration:
                poisonedDuration -= (lastPoisonedAt + duration - t)
            poisonedDuration += duration
            lastPoisonedAt = t
        return poisonedDuration