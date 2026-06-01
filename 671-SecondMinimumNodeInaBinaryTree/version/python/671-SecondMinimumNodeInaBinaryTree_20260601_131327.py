# Last updated: 6/1/2026, 1:13:27 PM
# Binary Tree with recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(N)
9Space: O(H), in this case is O(logN)
10"""
11class Solution:
12    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
13        if not root:
14            return -1
15        if not root.left:
16            left = -1
17        if not root.right:
18            right = -1
19        if root.left and root.right:
20            left = root.left.val
21            right = root.right.val
22        if left == root.val:
23            left = self.findSecondMinimumValue(root.left)
24        if right == root.val:
25            right = self.findSecondMinimumValue(root.right)
26        if left == -1:
27            return right
28        if right == -1:
29            return left
30        return min(left, right)