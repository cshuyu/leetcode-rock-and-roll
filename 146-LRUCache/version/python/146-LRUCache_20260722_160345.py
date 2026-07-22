# Last updated: 7/22/2026, 4:03:45 PM
# DoublyLinkedList
1"""
2Time: get:O(1), put:O(1)
3Space: O(n)
4"""
5class Node:
6    def __init__(self, key=0, value=0):
7        self.key = key
8        self.value = value
9        self.prev = None
10        self.next = None
11
12class LRUCache:
13
14    def __init__(self, capacity: int):
15        self.capacity = capacity 
16        self.cache = {}
17        self.head = Node()
18        self.tail = Node()
19        self.head.next = self.tail
20        self.tail.prev = self.head
21
22    def _remove(self, node):
23        next = node.next
24        prev = node.prev
25        next.prev = prev
26        prev.next = next
27
28    def _add_to_tail(self, node):
29        self.tail.prev.next = node
30        node.prev = self.tail.prev
31        self.tail.prev = node
32        node.next = self.tail
33    
34    def get(self, key: int) -> int:
35        if key in self.cache:
36            node = self.cache[key]
37            self._remove(node)
38            self._add_to_tail(node)
39            return node.value
40        else:    
41            return -1
42
43    def put(self, key: int, value: int) -> None:
44        if key in self.cache:
45            self.cache[key].value = value
46            self._remove(self.cache[key])
47            self._add_to_tail(self.cache[key])
48            return
49
50        if len(self.cache) >= self.capacity:
51            least_used_node = self.head.next
52            self._remove(least_used_node)
53            del self.cache[least_used_node.key]
54
55        new_node = Node(key, value)         
56        self.cache[key] = new_node
57        self._add_to_tail(new_node) 
58
59
60# Your LRUCache object will be instantiated and called as such:
61# obj = LRUCache(capacity)
62# param_1 = obj.get(key)
63# obj.put(key,value)
64