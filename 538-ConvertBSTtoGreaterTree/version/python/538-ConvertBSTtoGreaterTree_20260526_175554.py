# Last updated: 5/26/2026, 5:55:54 PM
# BST+InOrderTraverse+Recursion
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
12    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
13        self.sum = 0
14        if not root:
15            return root
16
17        def traverse(node):
18            if node.right:
19                traverse(node.right)
20            self.sum += node.val
21            node.val = self.sum
22            if node.left:
23                traverse(node.left)
24        
25        traverse(root)
26        return root
27
28        