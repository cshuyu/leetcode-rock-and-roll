# Last updated: 5/7/2026, 12:11:00 AM
# LRU: 2nd Try
1class Node:
2    def __init__(self, key, val):
3        self.key = key
4        self.val = val
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
16    def remove(self, node):
17        node.prev.next = node.next
18        node.next.prev = node.prev
19        self.size -=1
20    
21    def addLast(self, node):
22        self.tail.prev.next = node
23        node.prev = self.tail.prev
24        self.tail.prev = node
25        node.next = self.tail
26        self.size += 1
27    
28    def deleteFirst(self):
29        lru = self.head.next
30        self.head.next = lru.next
31        lru.next.prev = self.head 
32        self.size -= 1
33        return lru
34
35class LRUCache:
36    def __init__(self, capacity: int):
37       self.map = {}
38       self.doubleLinkedLst = DoubleLinkedList()
39       self.capacity = capacity
40
41    def get(self, key: int) -> int:
42        if key in self.map:
43            node = self.map[key]
44            # remove the existing node
45            self.doubleLinkedLst.remove(node)
46            # add new node at the last
47            self.doubleLinkedLst.addLast(node)
48            return node.val
49        else:
50            return -1
51
52    def put(self, key: int, value: int) -> None:
53        if key in self.map:
54            # remove the existing node
55            existing_node = self.map[key]
56            self.doubleLinkedLst.remove(existing_node)
57            
58        # delete the first node
59        if self.doubleLinkedLst.size == self.capacity:
60            lru = self.doubleLinkedLst.deleteFirst()
61            lru_key = lru.key 
62            self.map.pop(lru_key)
63
64        
65        # add new node at the last
66        node = Node(key, value)
67        self.doubleLinkedLst.addLast(node)
68        self.map[key] = node
69
70
71# Your LRUCache object will be instantiated and called as such:
72# obj = LRUCache(capacity)
73# param_1 = obj.get(key)
74# obj.put(key,value)