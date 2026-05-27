# Last updated: 5/27/2026, 2:11:04 PM
# BST with space optimization
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time Complexity: O(H)
9Optimize the space complexity: O(1)
10"""
11class Solution:
12    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
13        if not root:
14            return TreeNode(val)
15        curr = root
16        while True:
17            if curr.val == val:
18                break
19            if curr.val > val:
20                if curr.left:
21                    curr = curr.left
22                else:
23                    curr.left = TreeNode(val)
24                    break
25            else:
26                if curr.right:
27                    curr = curr.right
28                else:
29                    curr.right = TreeNode(val)
30                    break
31        return root
32
33
34
35        