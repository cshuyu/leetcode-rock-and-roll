# Last updated: 7/12/2026, 4:50:40 PM
# Two pointers + heap
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6"""
7when we push val to a heap, if two nodes have the same value, it needs the second element as a tie-breaker;
8Time:O(nlogk)
9Space:O(k)
10"""
11class Solution:
12    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
13        dummy = ListNode(-1)
14        min_heap = []
15
16        for i in range(len(lists)):
17            if lists[i]:
18                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
19        
20        pointer = dummy
21        while min_heap:
22            _, idx, curr_node = heapq.heappop(min_heap)
23            pointer.next = curr_node
24            pointer = pointer.next
25            if curr_node.next:
26                heapq.heappush(min_heap, (curr_node.next.val, idx, curr_node.next))
27        
28        return dummy.next
29
30