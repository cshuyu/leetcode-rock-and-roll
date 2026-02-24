# Last updated: 2/23/2026, 6:44:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next==None:
            return None
        prev = ListNode(-1, head)
        i = j = prev
        while j.next and j.next.next:
            i = i.next
            j = j.next.next
        i.next = i.next.next
        return prev.next

               