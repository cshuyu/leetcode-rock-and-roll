# Last updated: 5/23/2026, 7:10:52 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7import heapq
8
9# Definition for singly-linked list.
10class ListNode:
11    def __init__(self, val=0, next=None):
12        self.val = val
13        self.next = next
14
15class Solution:
16    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
17        min_heap = []
18        counter = 0  # Crucial tie-breaker to prevent Python comparison crashes
19        
20        # Step 1: Push the head of each non-empty list into the heap
21        for head in lists:
22            if head:
23                heapq.heappush(min_heap, (head.val, counter, head))
24                counter += 1
25                
26        # Create a dummy node to easily build the result list
27        dummy = ListNode(0)
28        current = dummy
29        
30        # Step 2: Pop the smallest node, advance its pointer, and repeat
31        while min_heap:
32            val, _, node = heapq.heappop(min_heap)
33            
34            # Append to our result chain
35            current.next = node
36            current = current.next
37            
38            # If the popped node has a neighbor, push it in
39            if node.next:
40                heapq.heappush(min_heap, (node.next.val, counter, node.next))
41                counter += 1
42                
43        return dummy.next
44
45
46
47
48
49