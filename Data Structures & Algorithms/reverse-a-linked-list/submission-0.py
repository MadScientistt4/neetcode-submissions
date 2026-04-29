# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        cur = head
        prev = None
        temp = cur
        while cur.next:
            nexts = cur.next
            cur.next = prev
            prev = cur
            cur = nexts
            
        cur.next = prev
        head = cur
        return head