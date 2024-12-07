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
        mapCopy ={}
        copy = dummy = ListNode()
        cur = head
        while cur:
            dummy.next = ListNode(cur.val)
            mapCopy[cur] = dummy.next
            dummy = dummy.next
            cur = cur.next
        copied = copy.next
        while head:
            random = head.random
            ran_val = None
            if ( random in mapCopy):
                ran_val = mapCopy[random] 
            copied.random = ran_val
            copied = copied.next

            head = head.next
        return copy.next
        