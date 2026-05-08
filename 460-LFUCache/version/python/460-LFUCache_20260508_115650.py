# Last updated: 5/8/2026, 11:56:50 AM
# LFU design: a freq dictionary of doubleLinkedList with a hashmap of key and node.
1class Node:
2    def __init__(self, key=None, val=None):
3        self.key = key
4        self.val = val
5        self.freq = 1
6        self.next = None
7        self.prev = None
8
9class DoubleLinkedLst:
10    def __init__(self):
11        self.size = 0
12        self.head = Node()
13        self.tail = Node()
14        self.head.next = self.tail
15        self.tail.prev = self.head
16
17    def remove(self, node):
18        node.prev.next = node.next
19        node.next.prev = node.prev
20        self.size -= 1
21
22    def addLast(self, node):
23        self.tail.prev.next = node
24        node.prev = self.tail.prev
25        self.tail.prev = node
26        node.next = self.tail
27        self.size += 1
28        
29    def deleteFirst(self):
30        if self.size == 0:
31            return None
32        node = self.head.next
33        self.remove(node)
34        return node
35
36class LFUCache:   
37    def __init__(self, capacity: int):
38        self.capacity = capacity
39        self.map = {}
40        self.freqLst = defaultdict(DoubleLinkedLst)
41        self.min_freq = 0
42
43    def _update(self, node):
44        """Helper to move a node to its new frequency list."""
45        freq = node.freq
46        # 1. Remove from old frequency list
47        self.freqLst[freq].remove(node)
48        
49        # 2. Update min_freq if the current list was the only one at that freq
50        if freq == self.min_freq and self.freqLst[freq].size == 0:
51            self.min_freq += 1
52        
53        # 3. Increase frequency and add to the new list
54        node.freq += 1
55        self.freqLst[node.freq].addLast(node)
56
57    def get(self, key: int) -> int:
58        if key in self.map:
59            node = self.map[key]
60            self._update(node)
61            return node.val
62        else:
63            return -1
64
65    def put(self, key: int, value: int) -> None:
66        if self.capacity == 0:
67            return
68
69        # update existing node
70        if key in self.map:
71            node = self.map[key]
72            node.val = value
73            self._update(node)
74            return
75
76        # if capacity is full, delete the lfu node
77        if len(self.map) == self.capacity:
78            min_freq_lst = self.freqLst[self.min_freq]
79            lfu = min_freq_lst.deleteFirst()
80            if lfu:
81                self.map.pop(lfu.key)
82
83        # add new Node 
84        new_node = Node(key, value)
85        self.min_freq = 1
86        self.freqLst[1].addLast(new_node)
87        self.map[new_node.key] = new_node
88              
89
90# Your LFUCache object will be instantiated and called as such:
91# obj = LFUCache(capacity)
92# param_1 = obj.get(key)
93# obj.put(key,value)
94
95