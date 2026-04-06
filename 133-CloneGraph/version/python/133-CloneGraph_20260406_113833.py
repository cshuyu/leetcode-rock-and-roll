# Last updated: 4/6/2026, 11:38:33 AM
# Graph: build graph by dfs
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        visited = {}
13        def dfs(node):
14            if not node:
15                return node
16            if node in visited:
17                return visited[node]
18            clone_node = Node(node.val, [])
19            visited[node] = clone_node
20            for neighbor in node.neighbors:
21                clone_node.neighbors.append(dfs(neighbor))
22            return clone_node
23        return dfs(node)