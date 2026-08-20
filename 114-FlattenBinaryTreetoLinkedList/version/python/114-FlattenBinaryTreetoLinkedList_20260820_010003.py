# Last updated: 8/20/2026, 1:00:03 AM
# Binary Tree: recursive
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
12    def flatten(self, root: Optional[TreeNode]) -> None:
13        """
14        Do not return anything, modify root in-place instead.
15        """
16        def helper(node):
17            if not node:
18                return None, None
19            left_root, left_tail = helper(node.left)
20            right_root, right_tail = helper(node.right)
21            node.left = None
22            if left_root:
23                node.right = left_root
24                if left_tail:
25                    left_tail.right = right_root
26            else:
27                node.right = right_root
28            if right_tail:
29                curr_tail = right_tail
30            elif left_tail:
31                curr_tail = left_tail
32            else:
33                curr_tail = node
34            return node, curr_tail
35        
36        helper(root)
37            
38