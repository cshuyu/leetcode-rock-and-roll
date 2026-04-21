# Last updated: 4/21/2026, 4:28:01 PM
# DFS with InOrder Traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        res = []
12        def dfs(node):
13            if node.left:
14                dfs(node.left)
15            res.append(node.val)
16            if node.right:
17                dfs(node.right)
18        dfs(root)
19        return res
20
21        