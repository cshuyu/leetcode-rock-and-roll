# Last updated: 5/27/2026, 1:25:07 PM
# BST
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time Complexity: O(h)
9Space Complexity: O(h)
10"""
11class Solution:
12    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
13        if not root:
14            return None
15        if root.val == val:
16            return root
17        if root.val < val:
18            return self.searchBST(root.right, val)
19        else:
20            return self.searchBST(root.left, val)