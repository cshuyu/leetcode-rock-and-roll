# Last updated: 5/31/2026, 11:57:23 PM
# BST
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8O(Time): O(N)
9O(Space): O(N)
10"""
11class Solution:
12    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
13        if root is None:
14            return None
15        if root.val<low:
16            return self.trimBST(root.right, low, high)
17        if root.val>high:
18            return self.trimBST(root.left, low, high)
19        root.left = self.trimBST(root.left, low, high)
20        root.right = self.trimBST(root.right, low, high)
21        return root
22        