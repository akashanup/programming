# Money Change

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is
to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.

### Example 1
```sh
Input: m = 34, coins = [1, 3, 4]
Output: 9
Explanation: 34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
```
