"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    #“Because each original node’s copy is placed right after it, the copy of any random target is just random.next.”
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy = ListNode(head.val)
        # ch = copy
         # 🔹 PASS 1: Interleave copied nodes
        #  A → B → C
        # ⬇
        # A → A' → B → B' → C → C'

        head1 = head
        
        while head1:
            copy = Node(head1.val, head1.next)
            head1.next = copy
            head1 = copy.next
        head1 = head
   
        while head1:
            
            random = head1.random
            if  random:
                head1.next.random = random.next
            head1 = head1.next.next
        
        # pass 3 - removingc copy from origina
        copy2 = None
        if head:
            copy2 = head.next
        head1 = head
        while head1:
            copy1 = head1.next
            head1 = copy1.next 
            if copy1.next:
                copy1.next = copy1.next.next
            
        return copy2

        
        