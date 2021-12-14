# Longest Duplicate Substring

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

### Example 1
```sh
Input: s = "banana"
Output: "ana"
```

### Example 2
```sh
Input: s = "acdnnefghnncdn"
Output: "cdn"
```

### Example 3
```sh
Input: s = "abcd"
Output: ""
```

### Constraints
```sh
2 <= s.length <= 3 * 104
s consists of lowercase English letters.
```