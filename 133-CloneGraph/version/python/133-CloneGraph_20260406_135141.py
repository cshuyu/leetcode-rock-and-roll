# Last updated: 4/6/2026, 1:51:41 PM
# Graph: build graph with bfs
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8'''
9Time Complexity: O(V+E)
10Space Complexity: O(V)
11'''
12from typing import Optional
13class Solution:
14    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
15        if not node:
16            return node
17        visited = {}
18        clone_node = Node(node.val, [])
19        node_queue = deque()
20        node_queue.append(node)
21        visited[node] = clone_node
22
23        while node_queue:
24            curr_node = node_queue.popleft()
25            curr_clone_node = visited[curr_node]
26            for neighbor in curr_node.neighbors:
27                if neighbor in visited:
28                    clone_neighbor = visited[neighbor]
29                else:
30                    clone_neighbor = Node(neighbor.val, [])
31                    node_queue.append(neighbor)
32                    visited[neighbor] = clone_neighbor
33                curr_clone_node.neighbors.append(clone_neighbor)
34        
35        return clone_node
36            
37                
38