# Last updated: 5/31/2026, 10:13:25 PM
# BST with inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9Space: O(h)
10"""
11class Solution:
12    def recoverTree(self, root: Optional[TreeNode]) -> None:
13        """
14        Do not return anything, modify root in-place instead.
15        """
16        # Left and right
17        self.prev = None
18        self.first = None
19        self.second = None
20
21        def inorderTraverse(node):
22            if not node:
23                return
24            inorderTraverse(node.left)
25            if self.prev and self.prev.val >= node.val:
26                if not self.first:
27                    self.first = self.prev
28                self.second = node
29            self.prev = node
30            inorderTraverse(node.right)
31        
32        inorderTraverse(root)
33        if self.first and self.second:
34            self.first.val, self.second.val = self.second.val, self.first.val
35    