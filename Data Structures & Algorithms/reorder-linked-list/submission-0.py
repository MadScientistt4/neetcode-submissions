# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur2 = slow.next
        slow.next = None
        prev = None
        while cur2:
            temp = cur2.next
            cur2.next = prev
            prev = cur2
            cur2 = temp
        head2, cur = prev, head

        while head2 and cur:
            tmp, tmp2 = cur.next, head2.next
            cur.next = head2
            head2.next = tmp
            head2 = tmp2
            cur = tmp
            





        

            

            

