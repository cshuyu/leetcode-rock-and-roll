# Last updated: 7/29/2026, 1:22:42 PM
1"""
2Time: O(n)
3Space: O(n)
4"""
5# Definition for a binary tree node.
6# class TreeNode:
7#     def __init__(self, val=0, left=None, right=None):
8#         self.val = val
9#         self.left = left
10#         self.right = right
11class Solution:
12    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
13        res = []
14        def inOrder(node):
15            if not node:
16                return
17            inOrder(node.left)
18            res.append(node.val)
19            inOrder(node.right)
20        inOrder(root)
21        return res[k-1]