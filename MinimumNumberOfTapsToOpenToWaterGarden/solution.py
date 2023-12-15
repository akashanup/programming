"""
Intuition
Idea is to solve this problem greedly with the help of a stack.
Stack will maintain the ranges(s, e) of taps required so far.

Approach
Before adding any new tap in the stack, we will check whether the current tap can accommodate the range of previous tap
in stack. If it can, then we remove the previous tap as it won't be any use now.
The Logic for accommodation would be if the range of previous tap lies in between the range of current tap.
If it does, then remove the previous. We have to repeat this till the current tap cannot accommodate the previous tap.
Now add the current tap in stack if stack is empty or the right range of current tap is more than the right range of
previous tap in stack.
Return the number of taps in stack if their range sum >= n, else -1

Complexity
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        stack = []
        for i, r in enumerate(ranges):
            s, e = max(0, i - r), min(n, i + r)
            if not stack:
                stack.append((s, e))
            else:
                while stack and s <= stack[-1][0] and e >= stack[-1][1]:
                    stack.pop()
                if not stack:
                    stack.append((s, e))
                elif e > stack[-1][1]:
                    # Max is done for the edge cases when tap's range is 0.
                    stack.append((max(s, stack[-1][1]), e))
        stack = [j - i for i, j in stack]
        return len(stack) if stack and sum(stack) >= n else -1

