# Lexicographically smallest string formed by appending a character from the first K characters of a given string

Given a string S consisting of lowercase alphabets. The task is to find the lexicographically smallest string X of the same length only that can be formed using the operation given below:
In a single operation, select any one character among the at most first K characters of string S, remove it from string S and append it to string X. Apply this operation as many times as he wants.

### Example 1
```sh
Input: str = "gaurang", k=3 
Output: agangru 
Remove "a" in the first step and append to X. 
Remove "g" in the second step and append to X. 
Remove "a" in the third step and append to X. 
Remove "n" in the third step and append to X. 
Pick the lexicographically smallest character at every step from the first K characters to get the 
string "agangru"
```

### Example 2
```sh
Input: str = "geeksforgeeks", k=5 
Output: eefggeekkorss
```
