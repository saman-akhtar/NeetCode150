# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        l = 0
        c =0
        while p:
            p = p.next
            l += 1
        if n > l:
            return head 
        count = l - n -1
        cur = head
        if count < 0:
            return head.next
        while count > 0 and cur:
            cur = cur.next
            count -= 1

        if cur.next:
                new_element = cur.next.next
                cur.next = new_element
         
        return head

 ## TC O(N)
 # SC O(`1`)

        
        



        