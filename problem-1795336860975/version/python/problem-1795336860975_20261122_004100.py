# Last updated: 11/22/2026, 12:41:00 AM
# File System: Trie
1class TrieNode:
2    def __init__(self):
3        self.children = {}
4        self.is_file = False
5        self.content = []
6
7class FileSystem:
8
9    def __init__(self):
10        self.root = TrieNode()
11    
12    def _traverse(self, path, create):
13        curr = self.root
14        if path == "/":
15            return curr
16        for part in path.split("/")[1:]:
17            if part not in curr.children:
18                if not create:
19                    return None
20                curr.children[part] = TrieNode()
21            curr = curr.children[part]
22        return curr
23
24    def ls(self, path: str) -> list[str]:
25        node = self._traverse(path, True)
26        if node.is_file:
27            return [path.split("/")[-1]]
28        return sorted(node.children.keys())
29
30    def mkdir(self, path: str) -> None:
31        self._traverse(path, True)
32
33    def addContentToFile(self, filePath: str, content: str) -> None:
34        node = self._traverse(filePath, create=True)
35        node.is_file = True
36        node.content.append(content)
37
38    def readContentFromFile(self, filePath: str) -> str:
39        node = self._traverse(filePath, False)
40        if node is None:
41            raise FileNotFoundError(f"no such file path: '{filepath}'")
42        if not node.is_file:
43            raise IsADirectoryError(f"{filepath} is not a file")
44        return "".join(node.content)
45
46
47# Your FileSystem object will be instantiated and called as such:
48# obj = FileSystem()
49# param_1 = obj.ls(path)
50# obj.mkdir(path)
51# obj.addContentToFile(filePath,content)
52# param_4 = obj.readContentFromFile(filePath)