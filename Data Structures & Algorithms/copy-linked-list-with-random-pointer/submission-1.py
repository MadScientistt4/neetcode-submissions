"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashset = {None: None} # old_pointer : new_pointer
        cur1 = head
        head_new = Node(0)
        cur = head_new
        while cur1:
            new_node = Node(cur1.val)
            cur.next = new_node
            hashset[cur1] = new_node
            cur1 = cur1.next
            cur = cur.next
        cur1 = head
        cur = head_new.next
        while cur1:
            cur.random = hashset[cur1.random]
            cur = cur.next
            cur1 = cur1.next
        return head_new.next