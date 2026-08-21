# Last updated: 8/21/2026, 10:37:05 AM
# Build_tree: recursion
1"""
2Time: O(n^2)
3Space: O(n)
4"""
5# Definition for a binary tree node.
6# class TreeNode:
7#     def __init__(self, val=0, left=None, right=None):
8#         self.val = val
9#         self.left = left
10#         self.right = right
11class Solution:
12    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
13        def build(start, end):
14            max_idx = start
15            if start > end:
16                return
17            for i in range(start+1, end+1):
18                if nums[i]>nums[max_idx]:
19                    max_idx = i
20            root = TreeNode(nums[max_idx])
21            root.left = build(start, max_idx-1)
22            root.right = build(max_idx+1, end)
23            return root
24        return build(0, len(nums)-1)