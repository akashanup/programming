# Find minimum number of coins that make a given value

Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make change, print -1. 

### Example 1
```sh
Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
Explanation: We can use one coin of 25 cents and one of 5 cents 
```

### Example 2
```sh
Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
Explanation: We can use one coin of 6 cents and one coin of 5 cents
```

### Example 3
```sh
Input: coins[] = {1, 2, 5, 10, 20, 50, 100, 500, 1000}, V = 93
Output: Minimum 2 coins required
Explanation: We can use one coin of 50 cents, two coin of 20 cents, one coin of 2 cents and one coins of 1 cent
```
