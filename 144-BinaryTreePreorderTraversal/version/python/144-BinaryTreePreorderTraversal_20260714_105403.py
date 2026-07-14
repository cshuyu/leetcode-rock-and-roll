# Last updated: 7/14/2026, 10:54:03 AM
# preOrder_traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8O(Time): O(n)
9O(Space): O(n)
10"""
11class Solution:
12    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
13        res = []
14        def helper(node, res):
15            if node is None:
16                return []
17            else:
18                res.append(node.val)
19                helper(node.left, res)
20                helper(node.right, res)
21            return res
22        return helper(root, res)
23        
24