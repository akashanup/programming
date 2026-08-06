"""
# Intuition
The problem follows a repeating pattern for every 2k characters:
- Reverse the first k characters.
- Keep the next k characters unchanged.

Instead of iterating in chunks of 2k, we can process the string in chunks of size k and alternate between reversing and not reversing each chunk using a boolean flag.

# Approach
1. Create an empty list revArr to store processed parts of the string.
2. Use a boolean variable needsReverse to track whether the current chunk should be reversed.
3. Iterate through the string in steps of size k.
4. If needsReverse is True, reverse the current substring using slicing [::-1].
5. Otherwise, append the substring as it is.
6. Toggle the boolean after each iteration.
7. Join all parts together and return the final string.

# Complexity
- Time complexity: $$O(n)$$. Each character is processed exactly once.

- Space complexity: $$O(n)$$. Extra space is used to store the resulting substrings.
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        revArr = []
        needsReverse = True
        for i in range(0, len(s), k):
            if needsReverse:
                revArr.append(s[i:i+k][::-1])
            else:
                revArr.append(s[i:i+k])
            needsReverse = not needsReverse
        return "".join(revArr)