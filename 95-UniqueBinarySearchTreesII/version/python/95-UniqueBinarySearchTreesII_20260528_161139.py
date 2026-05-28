# Last updated: 5/28/2026, 4:11:39 PM
# BST: recursion+memo
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8O(Time): O(4^n/n^0.5)
9O(Space): O(4^n/n^0.5) 
10stack is O(n), memo is O(4^n/n^0.5), which is n * all tree combinations
11"""
12class Solution:
13    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
14        self.memo = {}
15        def build(low, high):
16            res = []
17            if low>high:
18                res.append(None)
19                return res
20            if (low, high) in self.memo:
21                return self.memo[(low, high)]
22            for root in range(low, high+1):
23                left_tree_lst = build(low, root-1)
24                right_tree_lst = build(root+1, high)
25                for left_tree in left_tree_lst:
26                    for right_tree in right_tree_lst:
27                        root_node = TreeNode(root)
28                        root_node.left = left_tree
29                        root_node.right = right_tree
30                        res.append(root_node)
31            self.memo[(low, high)] = res
32            return res
33        return build(1, n)
34            