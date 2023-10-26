"""
Intuition:
Intuition behind this problem is straight forward. Let us say for a number n in arr we want to find all its factor pairs from arr. These factor pairs can vbe easily found by multiplying every number with another and if their product becomes equal to n then we have found a factor pair.
Now each number in the factor pairs can have its own list of factor pairs and so on and so forth.
Now assume this number as a root, and its factor pairs as left and right child of a binary tree.
So a recurrence relationship can be seen here-
Let's say the number n has factor pairs as (n1,n2) and (n3,n4). So the total number of different factor pairs can be formed for n is

binaryTree(n) = binaryTree(n1,n2) + binaryTree(n3,n4)
=> binaryTree(n) = binaryTree(n1)*binaryTree(n2) + binaryTree(n3)*binaryTree(n4) iff n1==n2 | n3==n4
=> binaryTree(n) = binaryTree(n1)*binaryTree(n2)*2

Approach:
Create a hashmap `binaryTrees` with only root nodes with the values of arr.
Now build this hashmap with keys as root and values as a list of a different possible left,right child combination from arr.
**Remember that root, left and right all must belong to arr only.**

Now we need to take one root at a time and calculate the number of all possible binary trees.
Now which root to take first becomes a question because there might be chances that the total number of binary trees for its children isn't calculated yet.
But we know that the root will always be the product of its children, which means the value of root will always be greater than the value of its children.
So if we choose the roots in sorted order, then we can guarantee that the total number of binary trees for children has already been calculated.
"""



class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        binaryTrees = {_: [(None, None)] for _ in arr}
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                root = arr[i] * arr[j]
                if root in binaryTrees:
                    binaryTrees[root].append((i, j))

        dp = {}
        count = 0
        for root in sorted(arr):
            for left, right in binaryTrees[root]:
                if left is None:
                    dp[root] = 1
                elif left == right:
                    dp[root] += (dp[arr[left]] * dp[arr[right]])
                else:
                    dp[root] += (dp[arr[left]] * dp[arr[right]] * 2)
            count += dp[root]

        return count % MOD

