# Last updated: 4/21/2026, 2:06:14 PM
# DFS with recurisive
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        res = []
12        stack = [root]
13        while stack:
14            node = stack.pop()
15            res.append(node.val)
16            if node.right:
17                stack.append(node.right)
18            if node.left:
19                stack.append(node.left)
20        return res