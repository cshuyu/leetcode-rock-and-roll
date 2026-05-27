# Last updated: 5/27/2026, 1:50:05 PM
# BST with recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time Complexity: O(H)
9Space Complexity: O(H)
10"""
11class Solution:
12    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
13        if not root:
14            return TreeNode(val)
15        if root.val == val:
16            return root
17        if root.val > val:
18            root.left = self.insertIntoBST(root.left, val)
19        else:
20            root.right = self.insertIntoBST(root.right, val)
21        return root
22        