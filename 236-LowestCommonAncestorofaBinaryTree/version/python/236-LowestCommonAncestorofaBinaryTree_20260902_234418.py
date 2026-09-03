# Last updated: 9/2/2026, 11:44:18 PM
# Tree: LCA
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7"""
8Time: O(n)
9Space: O(n)
10"""
11class Solution:
12    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
13        def find(node, p, q):
14            if not node:
15                return None
16            if node==p or node==q:
17                return node
18            left = find(node.left, p, q)
19            right = find(node.right, p, q)
20            if left and right:
21                return node
22            if not left:
23                return right
24            if not right:
25                return left
26        return find(root, p, q)
27