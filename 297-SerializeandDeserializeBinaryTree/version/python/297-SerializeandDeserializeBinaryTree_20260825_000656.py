# Last updated: 8/25/2026, 12:06:56 AM
# Tree serialization and deserialization
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7"""
8Both serialize and deserialize is O(n)
9"""
10class Codec:
11
12    def serialize(self, root):
13        """Encodes a tree to a single string.
14        
15        :type root: TreeNode
16        :rtype: str
17        """
18        res = []
19        def traverse(node):
20            if not node:
21                res.append("#")
22                return
23            res.append(str(node.val))
24            traverse(node.left)
25            traverse(node.right)
26        traverse(root)
27        return ",".join(res)
28
29    def deserialize(self, data):
30        """Decodes your encoded data to tree.
31        
32        :type data: str
33        :rtype: TreeNode
34        """
35        vals = deque(data.split(","))
36        def traverse():
37            val = vals.popleft()
38            if val == "#":
39                return None
40            node = TreeNode(int(val))
41            node.left = traverse()
42            node.right = traverse()
43            return node
44        return traverse()
45
46        
47
48# Your Codec object will be instantiated and called as such:
49# ser = Codec()
50# deser = Codec()
51# ans = deser.deserialize(ser.serialize(root))
52
53