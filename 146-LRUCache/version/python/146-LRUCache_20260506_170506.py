# Last updated: 5/6/2026, 5:05:06 PM
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
16class LRUCache:
17    def __init__(self, capacity: int):
18       self.map = {}
19       self.doubleLinkedLst = DoubleLinkedList()
20       self.capacity = capacity
21
22    def get(self, key: int) -> int:
23        if key in self.map:
24            node = self.map[key]
25            # remove the existing node
26            node.prev.next = node.next
27            node.next.prev = node.prev
28            self.doubleLinkedLst.size -= 1
29            # add new node at the last
30            self.doubleLinkedLst.tail.prev.next = node
31            node.prev = self.doubleLinkedLst.tail.prev
32            self.doubleLinkedLst.tail.prev = node
33            node.next = self.doubleLinkedLst.tail
34            self.doubleLinkedLst.size += 1
35            return node.val
36        else:
37            return -1
38
39    def put(self, key: int, value: int) -> None:
40        if key in self.map:
41            # remove the existing node
42            existing_node = self.map[key]
43            existing_node.prev.next = existing_node.next
44            existing_node.next.prev = existing_node.prev
45            self.doubleLinkedLst.size -= 1
46            
47        # delete the first node
48        if self.doubleLinkedLst.size == self.capacity:
49            lru = self.doubleLinkedLst.head.next
50            lru_key = lru.key
51            self.doubleLinkedLst.head.next = lru.next
52            lru.next.prev = self.doubleLinkedLst.head 
53            self.map.pop(lru_key)
54            self.doubleLinkedLst.size -= 1
55        
56        # add new node at the last
57        node = Node(key, value)
58        self.doubleLinkedLst.tail.prev.next = node
59        node.prev = self.doubleLinkedLst.tail.prev
60        self.doubleLinkedLst.tail.prev = node
61        node.next = self.doubleLinkedLst.tail
62        self.map[key] = node
63        self.doubleLinkedLst.size += 1
64
65
66# Your LRUCache object will be instantiated and called as such:
67# obj = LRUCache(capacity)
68# param_1 = obj.get(key)
69# obj.put(key,value)