# Last updated: 7/15/2026, 3:19:21 PM
# Binary Tree: BFS
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7"""
8Time: O(n)
9Space: O(n)
10"""
11class Solution:
12    def minDepth(self, root: Optional[TreeNode]) -> int:
13        if not root:
14            return 0
15        node_queue = deque()
16        node_queue.append((root,1))
17        min_depth = float("inf")
18        while node_queue:
19            curr, depth = node_queue.popleft()
20            if not curr.left and not curr.right:
21                min_depth = min(min_depth, depth)
22                return min_depth
23            if curr.left:
24                node_queue.append((curr.left, depth+1))
25            if curr.right:
26                node_queue.append((curr.right, depth+1))
27
28        return min_depth        
29