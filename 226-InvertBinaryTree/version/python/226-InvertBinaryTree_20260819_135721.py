# Last updated: 8/19/2026, 1:57:21 PM
# Binary_tree_recursive
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9Space: O(n)
10"""
11class Solution:
12    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
13        def traverse(node):
14            if not node:
15                return
16            tmp = node.left
17            node.left = node.right
18            node.right = tmp
19            traverse(node.left)
20            traverse(node.right)
21        traverse(root)
22        return root