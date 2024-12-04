# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        d= cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        r = l - n
        if r == 0:
            return head.next
        while r != 0:
            
            r -=1
            if( r == 0):
                d.next = d.next.next
            else:
                d = d.next

        return head

# TC O(N) = O(N) + O(N)
# SC O(1)    