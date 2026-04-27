# Last updated: 4/27/2026, 12:47:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        if not root:
11            return []
12        parent_map = {}
13        def findParents(node, parent=None):
14            parent_map[node] = parent
15            if node.left:
16                findParents(node.left, node)
17            if node.right:
18                findParents(node.right, node)
19
20        findParents(root, None)
21        dq = deque()
22        dq.append((target, 0))
23        visited = set()
24        visited.add(target)
25        res = []
26        while dq:
27            level_len = len(dq)
28            for i in range(level_len):
29                curr_node, distance = dq.popleft()
30                if distance == k:
31                    res.append(curr_node.val)
32                    continue
33                if curr_node.left and curr_node.left not in visited :
34                    dq.append((curr_node.left, distance+1))
35                    visited.add(curr_node.left)
36                if curr_node.right and curr_node.right not in visited:
37                    dq.append((curr_node.right, distance+1))
38                    visited.add(curr_node.right)
39                if parent_map[curr_node] and parent_map[curr_node] not in visited:
40                    dq.append((parent_map[curr_node], distance+1))
41                    visited.add(parent_map[curr_node])
42
43        return res
44            
45
46