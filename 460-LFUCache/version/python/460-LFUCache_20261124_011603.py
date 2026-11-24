# Last updated: 11/24/2026, 1:16:03 AM
# Two Hashmap+DoublyLinkedList
1'''
2O(time): O(1)
3O(space):O(Capacity)
4'''
5class Node:
6    def __init__(self, key=0, val=0, freq=1):
7        self.prev = None
8        self.next = None
9        self.key = key
10        self.val = val
11        self.freq = freq
12
13
14class DoublyLinkedList:
15    def __init__(self):
16        self.head = Node()
17        self.tail = Node()
18        self.head.next = self.tail
19        self.tail.prev = self.head
20        self.size = 0
21    
22    def _remove_node(self, node):
23        node.prev.next = node.next
24        node.next.prev = node.prev
25        self.size -= 1
26    
27    def _add_to_head(self, node):
28        node.next = self.head.next
29        self.head.next.prev = node
30        node.prev = self.head
31        self.head.next = node
32        self.size += 1
33    
34    def _pop_tail(self):
35        if self.size == 0:
36            return None
37        pop_node = self.tail.prev
38        self._remove_node(pop_node)
39        return pop_node
40
41
42class LFUCache:
43    
44    def __init__(self, capacity: int):
45        self.freq_to_list = defaultdict(DoublyLinkedList)
46        self.key_to_node = {}
47        self.capacity = capacity
48        self.min_freq = 0
49    
50    def _update_freq(self, node):
51        old_freq = node.freq
52        old_list = self.freq_to_list[old_freq]
53        old_list._remove_node(node)
54        if old_list.size == 0:
55            del self.freq_to_list[old_freq]
56            if self.min_freq == old_freq:
57                self.min_freq += 1
58        node.freq += 1
59        self.freq_to_list[node.freq]._add_to_head(node)
60
61    def get(self, key: int) -> int:
62        if key not in self.key_to_node:
63            return -1
64        curr_node = self.key_to_node[key]
65        self._update_freq(curr_node) 
66        return curr_node.val
67
68    def put(self, key: int, value: int) -> None:
69        if self.capacity == 0:
70            return
71
72        if key in self.key_to_node:
73            node = self.key_to_node[key]
74            node.val = value
75            self._update_freq(node)
76            return
77        
78        if len(self.key_to_node) == self.capacity:
79            min_list = self.freq_to_list[self.min_freq]
80            pop_node = min_list._pop_tail()
81            del self.key_to_node[pop_node.key]
82            if min_list.size == 0:
83                del self.freq_to_list[self.min_freq]
84
85        new_node = Node(key=key, val=value, freq=1)
86        self.key_to_node[key] = new_node
87        self.freq_to_list[1]._add_to_head(new_node)
88        self.min_freq = 1
89
90
91# Your LFUCache object will be instantiated and called as such:
92# obj = LFUCache(capacity)
93# param_1 = obj.get(key)
94# obj.put(key,value)