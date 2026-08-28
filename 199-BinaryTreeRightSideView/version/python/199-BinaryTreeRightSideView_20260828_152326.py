# Last updated: 8/28/2026, 3:23:26 PM
# DFS with right view
1"""
2Time: O(n)
3Space: O(h)
4"""
5# Definition for a binary tree node.
6# class TreeNode:
7#     def __init__(self, val=0, left=None, right=None):
8#         self.val = val
9#         self.left = left
10#         self.right = right
11class Solution:
12    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
13        res = []
14        def dfs(node, depth):
15            if not node:
16                return
17            if depth == len(res):
18                res.append(node.val)
19            dfs(node.right, depth+1)
20            dfs(node.left, depth+1)
21        dfs(root, 0)
22        return res