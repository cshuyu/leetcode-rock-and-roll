# Last updated: 11/5/2026, 12:45:14 AM
# recursive_traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7'''
8O(Time): O(n)
9O(Space): O(h)
10'''
11class Solution:
12    def isSymmetric(self, root: TreeNode | None) -> bool:
13        if root is None:
14            return True
15        
16        def helper(node_a, node_b):
17            if node_a is None and node_b is None:
18                return True
19            elif node_a is None and node_b is not None:
20                return False
21            elif node_a is not None and node_b is None:
22                return False
23            elif node_a.val != node_b.val:
24                return False
25            else: 
26                return helper(node_a.left, node_b.right) and helper(node_a.right, node_b.left)
27
28        return helper(root.left, root.right)