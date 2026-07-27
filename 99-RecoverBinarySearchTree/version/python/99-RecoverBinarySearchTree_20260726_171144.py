# Last updated: 7/26/2026, 5:11:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def recoverTree(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        self.prev = None
13        self.first = None
14        self.second = None
15
16        def inorder(node):
17            if not node:
18                return
19            inorder(node.left)
20            if self.prev and self.prev.val > node.val:
21                if not self.first:
22                    self.first = self.prev
23                self.second = node
24            self.prev = node
25            inorder(node.right)
26
27        inorder(root)
28        if self.first and self.second:
29            self.first.val, self.second.val = self.second.val, self.first.val
30