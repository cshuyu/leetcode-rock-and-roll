# Last updated: 7/30/2026, 12:35:53 AM
1"""
2Time: O(H)
3Space: O(H)
4"""
5# Definition for a binary tree node.
6# class TreeNode:
7#     def __init__(self, val=0, left=None, right=None):
8#         self.val = val
9#         self.left = left
10#         self.right = right
11class Solution:
12    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
13        if not root:
14            return None
15
16        if key < root.val:
17            root.left = self.deleteNode(root.left, key)
18        elif key > root.val:
19            root.right = self.deleteNode(root.right, key)
20        else:
21            if not root.left:
22                return root.right
23            if not root.right:
24                return root.left
25
26            successor = root.right
27            while successor.left:
28                successor = successor.left
29            root.val = successor.val
30            root.right = self.deleteNode(root.right, successor.val)
31        
32        return root 
33