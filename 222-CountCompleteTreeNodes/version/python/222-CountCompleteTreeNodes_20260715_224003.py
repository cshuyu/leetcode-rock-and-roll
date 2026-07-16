# Last updated: 7/15/2026, 10:40:03 PM
# Binary_Tree: complete_tree
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8O(Time): O(n)
9O(Space): O(1)
10"""
11class Solution:
12    def countNodes(self, root: Optional[TreeNode]) -> int:
13        if not root:
14            return 0
15        hl = hr = 0
16        l_node = r_node = root
17        while l_node is not None:
18            l_node = l_node.left
19            hl += 1
20        
21        while r_node is not None:
22            r_node = r_node.right
23            hr += 1
24
25        if hl == hr:
26            return pow(2, hl)-1
27        else:
28            return 1 + self.countNodes(root.left) + self.countNodes(root.right)