# Last updated: 4/24/2026, 11:58:42 PM
# BFS with transformation to graph problem
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
10        # 1. 建立父节点映射
11        parent_map = {}
12        def find_parents(node, par=None):
13            if node:
14                parent_map[node] = par
15                find_parents(node.left, node)
16                find_parents(node.right, node)
17        
18        find_parents(root)
19        
20        # 2. 从 target 开始 BFS
21        queue = deque([(target, 0)]) # (当前节点, 距离)
22        visited = {target} # 避免往回走导致死循环
23        res = []
24        
25        while queue:
26            node, dist = queue.popleft()
27            
28            if dist == k:
29                res.append(node.val)
30            elif dist < k:
31                # 检查三个邻居：左、右、父
32                for neighbor in [node.left, node.right, parent_map[node]]:
33                    if neighbor and neighbor not in visited:
34                        visited.add(neighbor)
35                        queue.append((neighbor, dist + 1))
36        
37        return res