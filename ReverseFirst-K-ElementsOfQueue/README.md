# Reverse First K elements of Queue

You are given a QUEUE containing ‘N’ integers and an integer ‘K’. 
You need to reverse the order of the first ‘K’ elements of the queue, leaving the other elements in the same relative order.

You can only use the standard operations of the QUEUE STL.
1. enqueue(x) : Adds an item x to rear of the queue
2. dequeue() : Removes an item from front of the queue
3. size() : Returns number of elements in the queue.
4. front() : Finds the front element.

For Example-
Let the given queue be { 1, 2, 3, 4, 5 } and K be 3.
You need to reverse the first K integers of Queue which are 1, 2, and 3.
Thus, the final response will be { 3, 2, 1, 4, 5 }.


### Example 1
```sh
Input: queue = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
```

### Example 2
```sh
Input: queue = [6, 2, 4, 1], k = 2
Output: [2, 6, 4, 1]
```

### Constraints
```sh
1 <= T <= 10
1 <= N <= 10^5
0 <= K <= N
-10^9 <= queue elements <= 10^9
```
