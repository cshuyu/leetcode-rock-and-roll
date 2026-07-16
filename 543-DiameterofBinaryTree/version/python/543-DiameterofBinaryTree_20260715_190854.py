# Last updated: 7/15/2026, 7:08:54 PM
# Binary_tree: recursion
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
12    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
13        if root == None:
14            return 0
15        self.max_dia = 0
16
17        def maxHeight(node):
18            if node is None:
19                return 0
20            max_left = maxHeight(node.left)
21            max_right = maxHeight(node.right)
22            curr_dia = max_left+max_right
23            self.max_dia = max(self.max_dia, curr_dia)
24            return 1+max(max_left, max_right)
25        
26        maxHeight(root)
27        return self.max_dia