# Last updated: 5/27/2026, 2:57:03 PM
# BST with recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time Complexity: O(H)
9Space Complexity: O(H)
10"""
11class Solution:
12    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
13        if not root:
14            return root
15        
16        def getMinNode(node):
17            while node.left:
18                node = node.left
19            return node
20
21        if root.val == key:
22            if not root.left:
23                return root.right
24            if not root.right:
25                return root.left
26            min_right = getMinNode(root.right)
27            root.right = self.deleteNode(root.right, min_right.val)
28            min_right.left = root.left
29            min_right.right = root.right
30            return min_right
31        if root.val > key:
32            root.left = self.deleteNode(root.left, key)
33        if root.val < key:
34            root.right = self.deleteNode(root.right, key)
35        return root
36        