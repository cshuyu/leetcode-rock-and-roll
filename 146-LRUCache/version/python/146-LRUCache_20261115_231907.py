# Last updated: 11/15/2026, 11:19:07 PM
# LRU: DoublyLinkedList + hashmap
1'''
2O(Time): O(get), O(put) are both O(1)
3O(Space): O(n)
4'''
5class LRUCache:
6    def __init__(self, capacity: int):
7        self.capacity = capacity
8        self.cache = {}
9        self.head = LRUNode(-1, -1)
10        self.tail = LRUNode(-1, -1)
11        self.head.next = self.tail
12        self.tail.prev = self.head
13    
14    def _remove_node(self, curr_node):
15        curr_node.prev.next = curr_node.next
16        curr_node.next.prev = curr_node.prev
17    
18    def _add_to_tail(self, curr_node):
19        curr_node.prev = self.tail.prev
20        self.tail.prev.next = curr_node
21        curr_node.next = self.tail
22        self.tail.prev = curr_node
23
24    def _move_to_tail(self, curr_node):
25        self._remove_node(curr_node)
26        self._add_to_tail(curr_node)
27
28    def get(self, key: int) -> int:
29        if key not in self.cache:
30            return -1
31        curr_node = self.cache[key]
32        self._move_to_tail(curr_node)
33        return curr_node.val
34
35    def put(self, key: int, value: int) -> None:
36        if key in self.cache:
37            curr_node = self.cache[key]
38            curr_node.val = value
39            self._move_to_tail(curr_node)
40            return
41        
42        new_node = LRUNode(key, value)
43        self._add_to_tail(new_node)
44        self.cache[key] = new_node
45
46        if len(self.cache) > self.capacity:
47            least_node = self.head.next
48            self._remove_node(least_node)
49            del self.cache[least_node.key]
50
51
52class LRUNode:
53    def __init__(self, key, val):
54        self.key = key
55        self.val = val
56        self.prev = None
57        self.next = None       
58
59
60# Your LRUCache object will be instantiated and called as such:
61# obj = LRUCache(capacity)
62# param_1 = obj.get(key)
63# obj.put(key,value)
64
65