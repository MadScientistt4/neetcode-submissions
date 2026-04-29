# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new = ListNode(0, head)
        grpprev = new
        while True:
            kth = self.getkth(grpprev, k)
            if not kth:
                break
            grpnxt = kth.next
            prev, cur = kth.next, grpprev.next
            while cur != grpnxt:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            tmp = grpprev.next
            grpprev.next = kth
            grpprev = tmp
        return new.next
        
    def getkth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        

            
