# Last updated: 5/27/2026, 11:34:36 AM
# BST with inOrder recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8"""
9Time Complexity is O(n)
10Space Complexity is O(h)
11"""
12class Solution:
13    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
14        self.sum = 0
15        if not root:
16            return root
17        # Helper function    
18        def traverse(node):
19            if node.right:
20                traverse(node.right)
21            self.sum += node.val
22            node.val = self.sum
23            if node.left:
24                traverse(node.left)
25        traverse(root)
26        return root
27
28