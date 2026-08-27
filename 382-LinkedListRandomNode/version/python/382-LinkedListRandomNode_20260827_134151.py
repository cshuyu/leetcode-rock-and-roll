# Last updated: 8/27/2026, 1:41:51 PM
# Random
1"""
2O(Time): O(n)
3O(Space): O(1)
4"""
5# Definition for singly-linked list.
6# class ListNode:
7#     def __init__(self, val=0, next=None):
8#         self.val = val
9#         self.next = next
10class Solution:
11
12    def __init__(self, head: Optional[ListNode]):
13        self.head = head
14
15    def getRandom(self) -> int:
16        curr = self.head
17        res = self.head.val
18        i = 1
19        while curr:
20            if random.randint(0, i-1) == 0:
21                res = curr.val
22            curr = curr.next
23            i += 1
24        return res
25
26# Your Solution object will be instantiated and called as such:
27# obj = Solution(head)
28# param_1 = obj.getRandom()