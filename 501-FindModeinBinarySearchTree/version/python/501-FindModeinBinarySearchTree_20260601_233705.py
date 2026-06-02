# Last updated: 6/1/2026, 11:37:05 PM
# BFS with inorder traverse
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9Space: O(h)-->O(n)
10"""
11class Solution:
12    def findMode(self, root: Optional[TreeNode]) -> List[int]:
13        self.prev = None
14        self.maxCount = 0
15        self.currCount = 0
16        self.mode = []
17
18        def traverse(node):
19            if node is None:
20                return
21            traverse(node.left)
22
23            if self.prev is None:
24                self.maxCount = 1
25                self.currCount = 1
26                self.mode.append(node.val)
27            else:
28                if self.prev.val == node.val:
29                    self.currCount += 1
30                else:
31                    self.currCount = 1
32                if self.currCount == self.maxCount:
33                    self.mode.append(node.val)
34                if self.currCount > self.maxCount:
35                    self.maxCount = self.currCount
36                    self.mode = []
37                    self.mode.append(node.val)
38            self.prev = node
39
40            traverse(node.right)
41        
42        traverse(root)
43        return self.mode
44
45
46
47                
48
49        