# Find Smallest Letter Greater Than Target

Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

- For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.

### Example 1
```sh
Input: letters = ["c","f","j"], target = "a"
Output: "c"
```

### Example 2
```sh
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: changed is not a doubled array.
```

### Example 3
```sh
Input: letters = ["c","f","j"], target = "d"
Output: "f"
```

### Example 4
```sh
Input: letters = ["c","f","j"], target = "g"
Output: "j"
```

### Example 5
```sh
Input: letters = ["c","f","j"], target = "j"
Output: "c"
```

### Constraints
```sh
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
```
