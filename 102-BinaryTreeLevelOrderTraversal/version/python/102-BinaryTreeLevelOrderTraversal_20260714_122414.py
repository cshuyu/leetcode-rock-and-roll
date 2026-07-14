# Last updated: 7/14/2026, 12:24:14 PM
# Binary_Tree: level order
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
12    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
13        if root is None:
14            return []
15        res = []
16        node_queue = deque()
17        node_queue.append(root)
18        while node_queue:
19            level_nodes = []
20            level_len = len(node_queue)
21            pop_count = 0
22            while pop_count<level_len:
23                curr = node_queue.popleft()
24                level_nodes.append(curr.val)
25                if curr.left:
26                    node_queue.append(curr.left)
27                if curr.right:
28                    node_queue.append(curr.right)
29                pop_count += 1
30            res.append(level_nodes)
31        return res