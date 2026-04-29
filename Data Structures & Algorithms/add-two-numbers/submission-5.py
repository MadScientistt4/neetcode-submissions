# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        l3 = ListNode()
        cur3 = l3
        carry = 0
        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur3.next = ListNode(val)

            cur3 = cur3.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        return l3.next
