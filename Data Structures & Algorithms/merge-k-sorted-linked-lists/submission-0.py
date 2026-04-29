# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        res = []
        pos = 0
        head = ListNode()
        cur = head
        while lists:
            mini = float('inf')
            
            for i in range(n):
                if lists[i] and lists[i].val < mini:
                    mini = lists[i].val
                    pos = i
            if lists[pos]:
                print(lists[pos].val)
                cur.next = ListNode(lists[pos].val)
                cur = cur.next
                lists[pos] = lists[pos].next 
            else:
                break     
        return head.next