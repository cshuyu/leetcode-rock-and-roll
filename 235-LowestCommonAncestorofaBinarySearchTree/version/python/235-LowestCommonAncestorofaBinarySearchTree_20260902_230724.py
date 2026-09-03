# Last updated: 9/2/2026, 11:07:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        def find(node, p, q):
11            if not node:
12                return None
13            if node==p or node==q:
14                return node
15            left = find(node.left, p, q)
16            right = find(node.right, p, q)
17            if left and right:
18                return node
19            if not left:
20                return right
21            if not right:
22                return left
23        return find(root, p, q)
24
25        