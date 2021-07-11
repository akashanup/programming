# Check brackets in the code

In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the
code.

- Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
marks and brackets from the set []{}().
- Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise,
output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
brackets, output the 1-based index of the first unmatched opening bracket.

### Example 1
```sh
Input: s = "[]"
Output: "Success"
Explanation: The brackets are used correctly: there is just one pair of brackets [ and ], they correspond to each
other, the left bracket [ goes before the right bracket ], and no two pairs of brackets intersect, because
there is just one pair of brackets.
```

### Example 2
```sh
Input: s = "{[]}()"
Output: "Success"
Explanation: Here there are 3 pairs of brackets, one of them is nested into another one, and the third one is separate
from the first two.
```

### Example 3
```sh
Input: s = "{"
Output: 1
Explanation: The code { doesn’t use brackets correctly, because brackets cannot be divided into pairs (there is just
one bracket). There are no closing brackets, and the first unmatched opening bracket is {, and its
position is 1, so we output 1.
```

### Example 4
```sh
Input: s = "{[}"
Output: 3
Explanation: The bracket } is unmatched, because the last unmatched opening bracket before it is [ and not {. It
is the first unmatched closing bracket, and our first priority is to output the first unmatched closing
bracket, and its position is 3, so we output 3.
```

### Constraints
```sh
The length of 𝑆 is at least 1 and at most 10^5
```
