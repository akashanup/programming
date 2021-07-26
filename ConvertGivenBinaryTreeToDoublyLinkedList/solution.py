# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DoublyLinkedList:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def __init__(self):
        self.next = None
        self.prev = None

    def printDLL(self, head):
        while head:
            print(head.val, end=" ")
            head = head.right

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            if self.next:
                node = self.prev
                node.right = root
                node.right.left = node
                self.prev = node.right
            else:
                self.next = root
                self.prev = root
            self.inorder(root.right)
        return self.next

    def BToDLL(self, root):
        return self.inorder(root)


'''    
Time Complexity: The above program does a simple inorder traversal, so time complexity is O(n) where n is the number of nodes in given binary tree.
'''

tree = TreeNode(10)
tree.left = TreeNode(12)
tree.right = TreeNode(15)
tree.left.left = TreeNode(25)
tree.left.right = TreeNode(30)
tree.right.left = TreeNode(36)
head = Solution().BToDLL(tree)
Solution().printDLL(head)

