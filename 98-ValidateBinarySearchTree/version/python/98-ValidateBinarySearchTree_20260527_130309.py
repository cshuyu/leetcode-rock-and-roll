# Last updated: 5/27/2026, 1:03:09 PM
# BST with recursion min and max
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time Complexity: O(n)
9Space Complexity: O(h)
10"""
11class Solution:
12    def isValidBST(self, root: Optional[TreeNode]) -> bool:
13        if not root:
14            return True
15        def helper(node, min, max):
16            if min is not None and node.val<=min:
17                return False
18            if max is not None and node.val>=max:
19                return False
20            if node.left:
21                if not helper(node.left, min, node.val):
22                    return False
23            if node.right:
24                if not helper(node.right, node.val, max):
25                    return False
26            return True
27
28        return helper(root, None, None)