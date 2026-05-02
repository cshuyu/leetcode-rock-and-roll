# Last updated: 5/2/2026, 1:53:30 AM
# Hash LinkedList for LRU
1class Node:
2    def __init__(self, k, v):
3        self.key = k
4        self.val = v
5        self.next = None
6        self.prev = None
7
8class DoubleLinkedList:
9    def __init__(self):
10        self.head = Node(0, 0)
11        self.tail = Node(0, 0)
12        self.head.next = self.tail
13        self.tail.prev = self.head
14        self.size = 0
15
16class LRUCache:
17    def __init__(self, capacity: int):
18        self.cap = capacity
19        self.map = {}
20        self.cache = DoubleLinkedList()
21    
22    def makeRecent(self, key):
23        node = self.map[key]
24        node.prev.next = node.next
25        node.next.prev = node.prev
26        self.cache.tail.prev.next = node
27        node.prev = self.cache.tail.prev
28        node.next = self.cache.tail
29        self.cache.tail.prev = node
30
31    def addNew(self, key, value):
32        node = Node(key, value)
33        self.map[key] = node
34        self.cache.tail.prev.next = node
35        node.prev = self.cache.tail.prev
36        node.next = self.cache.tail
37        self.cache.tail.prev = node
38        self.cache.size += 1
39    
40    def delete(self, node):
41        prev_node = node.prev
42        next_node = node.next
43        prev_node.next = next_node
44        next_node.prev = prev_node
45        self.cache.size -= 1
46        self.map.pop(node.key)
47
48    def get(self, key: int) -> int:
49        if key not in self.map:
50            return -1
51        self.makeRecent(key)
52        return self.map[key].val
53        
54
55    def put(self, key: int, value: int) -> None:
56        if key in self.map:
57            self.map[key].val = value
58            self.makeRecent(key)
59        else:
60            if self.cache.size >= self.cap:
61                lru = self.cache.head.next
62                self.delete(lru)
63            self.addNew(key, value)
64
65
66# Your LRUCache object will be instantiated and called as such:
67# obj = LRUCache(capacity)
68# param_1 = obj.get(key)
69# obj.put(key,value)
70