# Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

### Example 1
```sh
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```

### Example 2
```sh
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```

### Example 3
```sh
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```

### Constraints
```sh
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
```

### Follow Up
```sh
Can you solve it in O(n) time and O(1) space?
```
