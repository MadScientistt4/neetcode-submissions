# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        distance_from_start = length - n
        if distance_from_start==0:
            return head.next
        count = 0
        prev = None
        cur = head
        while cur:
            if count == distance_from_start:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            count += 1
        return head
