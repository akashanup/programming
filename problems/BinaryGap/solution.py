"""
# Intuition
To find the longest binary gap, we first convert the number into its binary representation.
Then, we track the positions of every 1 in the binary string.
Whenever we encounter another 1, we calculate the distance from the previous 1 and update the maximum distance found so far.
The key idea is:
- Store the index of the last seen 1
- For every new 1, compute the gap between current index and previous index
- Keep the maximum gap

# Approach
1. Convert the integer n into a binary string using bin(n)[2:].
2. Initialize:
    - maxGap to store the maximum distance
    - lastOccuredOne to store the index of the previous 1

3. Find the first occurrence of 1.
4. Traverse the remaining binary string:
    - If the current character is 1
    - Calculate the distance from the previous 1
    - Update maxGap
    - Update lastOccuredOne to current index
5. Return maxGap.

# Complexity
- Time complexity: $$O(logn)$$. Since the number of bits in a binary representation of n is log n.
- Space complexity: $$O(logn)$$. We store the binary representation as a string.
"""

class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        maxGap = 0
        lastOccuredOne = -1
        for i in range(len(binary)):
            if binary[i] == "1":
                lastOccuredOne = i
                break
        for i in range(lastOccuredOne+1,len(binary)):
            if binary[i] == "1":
                maxGap = max(maxGap,i-lastOccuredOne)
                lastOccuredOne = i
        return maxGap