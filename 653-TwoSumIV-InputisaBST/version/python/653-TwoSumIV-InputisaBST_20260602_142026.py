# Last updated: 6/2/2026, 2:20:26 PM
# BFS with inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9space: O(n)
10"""
11class Solution:
12    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
13        self.rests = set()
14        self.is_equal = False
15
16        def traverse(node):
17            if not node:
18                return
19            traverse(node.left)
20            if self.rests and node.val in self.rests:
21                    self.is_equal = True
22            self.rests.add(k-node.val)
23            traverse(node.right)
24        
25        traverse(root)
26        return self.is_equal
27                
28            
29