# Last updated: 8/28/2026, 1:32:11 PM
# BFS with level traverse
1"""
2Time: O(n)
3Space: O(d), the diameter of the tree, the worst case is the binary tree, O(n)
4"""
5# Definition for a binary tree node.
6# class TreeNode:
7#     def __init__(self, val=0, left=None, right=None):
8#         self.val = val
9#         self.left = left
10#         self.right = right
11class Solution:
12    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
13        res = []
14        if not root:
15            return res
16        node_queue = deque()
17        node_queue.append(root)
18        while node_queue:
19            queue_size = len(node_queue)
20            for i in range(0, queue_size):
21                curr_node = node_queue.popleft()
22                if curr_node.left:
23                    node_queue.append(curr_node.left)
24                if curr_node.right:
25                    node_queue.append(curr_node.right)
26                if i==queue_size-1:
27                    res.append(curr_node.val)
28        return res