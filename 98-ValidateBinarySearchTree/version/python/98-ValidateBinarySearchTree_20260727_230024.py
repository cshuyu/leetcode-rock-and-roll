# Last updated: 7/27/2026, 11:00:24 PM
# BST: DFS
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
12    def isValidBST(self, root: Optional[TreeNode]) -> bool:
13        if not root:
14            return True
15        def helper(node, low, high):
16            if not node:
17                return True
18            if node.val <= low or node.val >= high:
19                return False
20            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
21        
22        return helper(root, float("-inf"), float("inf"))