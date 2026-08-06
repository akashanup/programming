# Palindrome Pairs

Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

### Example 1
```sh
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

### Example 2
```sh
Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
```

### Example 3
```sh
Input: words = ["a",""]
Output: [[0,1],[1,0]]
```

### Constraints
```sh
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
```
