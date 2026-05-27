# Last updated: 5/26/2026, 5:20:42 PM
# BST with recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time complexity is O(logn)
9Space complexity is O(logn)
10"""
11class Solution:
12    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
13        self.k = k
14        self.res = -1
15
16        def traverse(node):
17            # early exit if we have found the answer
18            if not node or self.res!=-1:
19                return
20            traverse(node.left)
21            self.k -= 1
22            if self.k==0:
23                self.res = node.val
24                return
25            traverse(node.right)
26
27        traverse(root)
28        return self.res
29
30
31
32        