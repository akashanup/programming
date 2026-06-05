"""
# Intuition
A perfect number is equal to the sum of all its positive divisors excluding itself.

Instead of checking every number from 1 to num - 1, we can optimize the solution by only iterating till sqrt(num) because divisors always occur in pairs.

For example, for 28:
- 2 and 14
- 4 and 7

If i divides num, then num // i is also a divisor.

# Approach
- Handle the edge case where num <= 1 since 1 is not a perfect number.
- Initialize divisorSum as 1 because 1 is always a divisor.
- Iterate from 2 to sqrt(num):
    - If i divides num evenly:
        - Add i
        - Add its paired divisor num // i
- Avoid adding the square root twice when both divisors are the same.
- Finally, compare divisorSum with num.
- 
# Complexity
- Time complexity: $$O(n ** 0.5​)$$

- Space complexity: $$O(1)$$
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False

        divisorSum = 1

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisorSum += i

                pairedDivisor = num // i

                if pairedDivisor != i:
                    divisorSum += pairedDivisor

        return divisorSum == num
