# Last updated: 6/2/2026, 9:54:40 AM
# BST wit inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        self.min_diff = float("inf")
10        self.prev = None
11
12        def traverse(node):
13            if node is None:
14                return
15            traverse(node.left)
16            if self.prev is not None:
17                self.min_diff = min(node.val-self.prev.val, self.min_diff)
18            self.prev = node
19            traverse(node.right)
20        
21        traverse(root)
22        return self.min_diff
23