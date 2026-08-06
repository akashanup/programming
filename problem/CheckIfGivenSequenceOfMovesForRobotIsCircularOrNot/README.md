# Check if a given sequence of moves for a robot is circular or not

Given a sequence of moves for a robot, check if the sequence is circular or not. A sequence of moves is circular if first and last positions of robot are same. A move can be on of the following. 

- G - Go one unit 
- L - Turn left
- R - Turn right 

### Example 1
```sh
Input: path[] = "GLGLGLG"
Output: True
Explanation: Given sequence of moves is circular.
```

### Example 2
```sh
Input: path[] = "GLRG"
Output: False
Explanation: Given sequence of moves is not circular.
```
