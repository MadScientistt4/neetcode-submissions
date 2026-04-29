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
        while cur1 and cur2:
            newNode = ListNode()
            if cur1.val + cur2.val + carry > 9:
                newNode.val = (cur1.val + cur2.val + carry) % 10
                carry = 1
            else:
                newNode.val = cur1.val + cur2.val + carry
                carry = 0
            cur1 = cur1.next
            cur2 = cur2.next
            cur3.next = newNode
            cur3 = cur3.next
        while cur1:
            if cur1.val + carry > 9:
                newNode = ListNode((cur1.val + carry)%10)
                carry = 1
            else:
                newNode = ListNode(cur1.val + carry)
                carry = 0
            cur1 = cur1.next
            cur3.next = newNode
            cur3 = cur3.next
        while cur2:
            if cur2.val + carry > 9:
                newNode = ListNode((cur2.val + carry)%10)
                carry = 1
            else:
                newNode = ListNode(cur2.val + carry)
                carry = 0
            cur2 = cur2.next
            cur3.next = newNode
            cur3 = cur3.next
        if carry == 1:
            newNode = ListNode(1)
            cur3.next = newNode
            
        return l3.next
