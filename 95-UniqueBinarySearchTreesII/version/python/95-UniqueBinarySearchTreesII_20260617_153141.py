# Last updated: 6/17/2026, 3:31:41 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8'''
9Time: O(n*Cn)
10Space: O(n*Cn)
11'''
12class Solution:
13    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
14        memo = {}
15        # [low, high)-> including low, but not high
16        def build(low, high):
17            if low==high:
18                return [None]
19            if (low, high) in memo:
20                return memo[(low, high)]
21            res = []
22            for node in range(low, high):
23                lefts = build(low, node)
24                rights= build(node+1, high)
25                for left in lefts:
26                    for right in rights:
27                        # Critical: create a new node for every combinations
28                        root = TreeNode(node)
29                        root.left = left
30                        root.right = right
31                        res.append(root)
32            memo[(low, high)] = res
33            return res
34        
35        return build(1, n+1)
36                