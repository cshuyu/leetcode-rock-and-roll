# Last updated: 2/23/2026, 6:44:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i = head
        j = head
        while j and j.next:
            j = j.next.next
            i = i.next
        mid = i
        prev = None
        while mid:
            tmp = mid.next
            mid.next= prev
            prev = mid
            mid = tmp
        max_sum = 0
        while prev:
            curr_sum = head.val + prev.val
            if curr_sum > max_sum:
                max_sum = curr_sum
            head = head.next
            prev = prev.next
        return max_sum