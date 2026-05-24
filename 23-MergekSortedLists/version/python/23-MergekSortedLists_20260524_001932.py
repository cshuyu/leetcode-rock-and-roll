# Last updated: 5/24/2026, 12:19:32 AM
# Heap
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6'''
7k is the number of the LinkedList
8Time: O(n*log(k))
9Space: O(k)
10'''
11class Solution:
12    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
13        minHeap = []
14        counter = 0
15        dummy = ListNode()
16        for head in lists:
17            if head:
18                heapq.heappush(minHeap, (head.val, counter, head))
19                counter += 1
20        
21        curr = dummy
22        while minHeap:
23            val, _, node = heapq.heappop(minHeap)
24            curr.next = node
25            curr = curr.next
26            if node.next:
27                heapq.heappush(minHeap, (node.next.val, counter, node.next))
28                counter += 1
29        
30        return dummy.next
31
32
33                