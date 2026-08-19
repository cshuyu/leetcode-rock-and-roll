# Last updated: 8/19/2026, 4:09:14 PM
# Binary_tree: recursive
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11"""
12Time: O(n)
13Space: O(n)
14"""
15class Solution:
16    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
17        if not root:
18            return root
19        def traverse(node1, node2):
20            if not node1 or not node2:
21                return
22            node1.next = node2
23            traverse(node1.left, node1.right)
24            traverse(node2.left, node2.right)
25            traverse(node1.right, node2.left)
26        traverse(root.left, root.right)
27        return root
28
29
30
31