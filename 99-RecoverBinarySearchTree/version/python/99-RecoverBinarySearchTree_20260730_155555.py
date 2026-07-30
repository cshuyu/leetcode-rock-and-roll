# Last updated: 7/30/2026, 3:55:55 PM
# Morris Traverse
1"""
2Morris Traverse
3Time: O(n)
4Space: O(1)
5"""
6# Definition for a binary tree node.
7# class TreeNode:
8#     def __init__(self, val=0, left=None, right=None):
9#         self.val = val
10#         self.left = left
11#         self.right = right
12class Solution:
13    def recoverTree(self, root: Optional[TreeNode]) -> None:
14        """
15        Do not return anything, modify root in-place instead.
16        """
17        first = second = prev = None
18        node = root
19        while node:
20            if not node.left:
21                if prev and prev.val>node.val:
22                    if not first:
23                        first = prev
24                    second = node
25                prev = node
26                node = node.right
27            else:
28                pred = node.left
29                while pred.right and pred.right is not node:
30                    pred = pred.right
31                if not pred.right:
32                    pred.right = node
33                    node = node.left
34                else:
35                    pred.right = None
36                    if prev and prev.val > node.val:
37                        if not first:
38                            first = prev
39                        second = node
40                    prev = node
41                    node = node.right
42        if first and second:
43            first.val, second.val = second.val, first.val
44