# Last updated: 5/28/2026, 4:02:18 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8O(Time): O(n^2)
9O(Space): O(n^3) stack is O(n), memo is O(n^2)*n 
10"""
11class Solution:
12    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
13        self.memo = {}
14        def build(low, high):
15            res = []
16            if low>high:
17                res.append(None)
18                return res
19            if (low, high) in self.memo:
20                return self.memo[(low, high)]
21            for root in range(low, high+1):
22                left_tree_lst = build(low, root-1)
23                right_tree_lst = build(root+1, high)
24                for left_tree in left_tree_lst:
25                    for right_tree in right_tree_lst:
26                        root_node = TreeNode(root)
27                        root_node.left = left_tree
28                        root_node.right = right_tree
29                        res.append(root_node)
30            self.memo[(low, high)] = res
31            return res
32        return build(1, n)
33            