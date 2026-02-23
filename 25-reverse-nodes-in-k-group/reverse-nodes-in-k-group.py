# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
      dummy = ListNode()  
     
      cur = head
      first = dummy
      while cur:
        n =k
        arr = []
        while cur and n > 0:
            arr.append(cur)
            cur = cur.next
            n -= 1
        if len(arr) == k:
            arr[0].next = arr[k-1].next
            first.next = arr[k-1]
            # cur = 
            first = arr[0]
            for i in range(k-1, 0,-1):
            
                arr[i].next = arr[i-1]

      return dummy.next  