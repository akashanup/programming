# Implement K Queues in a Single Array

You need to implement a data structure that represents K queues in a single array. 
The data structure should support the following operations.

- enqueue(int x, int Qn): Inserts an element x to queue number Qn where Qn ranges from 0 to K-1
- dequeue(int Qn): Deletes an element from queue number Qn where Qn ranges from 0 to K-1.

### Example 1
```sh
Input Q=2, N=5
    push(2, 1)
    push(3, 2)
    push(4, 1)
    pop(2)
    pop(1)

Output
    True
    True
    True
    3
    2
Explanation
    push(2, 1): Push element ‘2’ into the 1st queue. This returns true.
    push(3, 2): Push element ‘3’ into the 2nd queue. This returns true.
    push(4, 1): Push element ‘4’ into the 1st queue. This returns true.
    pop(2): Pop the top element from the 2nd queue. This returns 3.
    pop(1): Pop the top element from the 1st queue. This returns 2.
```

### Constraints
```sh
1 <= Q <= N <= 1000
1 <= X <= 10^5
```

