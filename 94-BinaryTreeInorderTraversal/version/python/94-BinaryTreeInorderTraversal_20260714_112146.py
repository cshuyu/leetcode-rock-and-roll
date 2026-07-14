# Last updated: 7/14/2026, 11:21:46 AM
# BST Inorder traverse
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
12    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
13        def helper(node, res):
14            if node is None:
15                return res
16            helper(node.left, res)
17            res.append(node.val)
18            helper(node.right, res)
19            return res
20        
21        res = []
22        return helper(root, res)