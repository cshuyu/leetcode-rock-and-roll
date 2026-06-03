# Last updated: 6/3/2026, 12:01:20 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def bstFromPreorder(self, preorder):
9        return self.build(preorder, 0, len(preorder) - 1)
10
11    def build(self, preorder, start, end):
12        if start > end:
13            return None
14
15        rootVal = preorder[start]
16        root = TreeNode(rootVal)
17
18        p = start + 1
19        while p <= end and preorder[p] < rootVal:
20            p += 1
21        # the range [start+1, p-1] contains elements of the left subtree
22        root.left = self.build(preorder, start + 1, p - 1)
23        # the range [p, end] contains elements of the right subtree
24        root.right = self.build(preorder, p, end)
25
26        return root    