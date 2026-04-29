# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head3 = cur3 = ListNode()
        cur1, cur2 = list1, list2 
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
            cur3 = cur3.next
        cur3.next = cur1 or cur2
        return head3.next



