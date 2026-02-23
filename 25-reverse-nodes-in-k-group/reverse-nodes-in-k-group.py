# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
    #   dummy = ListNode()  
     
    #   cur = head
    #   first = dummy
    #   while cur:
    #     n =k
    #     arr = []
    #     while cur and n > 0:
    #         arr.append(cur)
    #         cur = cur.next
    #         n -= 1
    #     if len(arr) == k:
    #         # first point to last elemet
    #         first.next = arr[k-1]
    #         arr[0].next = arr[k-1].next
            
            
    #         for i in range(k-1, 0,-1):
            
    #             arr[i].next = arr[i-1]
    #         first = arr[0]
    #     else:
    #         first.next =arr[0]


    #   return dummy.next  
# 
      # TC O(N)
      # SC O(K)


      # OPTIMIZED

        dummy = ListNode(0,head)  
        
        cur = head
        first = dummy

        def reverse(first,last):
            cur = first
            prev = last ## connect first to last element in array   
            while cur and cur != last:
                nxt = cur.next
                cur.next = prev
                
                prev = cur
                cur = nxt
            


        while cur:
            n = k
            grp_start = cur
            while cur and n > 1:
                cur = cur.next
                n -= 1
            # check if k element
            if not cur:
                break
            nxt = cur.next
            
            if n == 1:
                # make last element to first 
                first.next = cur
                
                reverse(grp_start, nxt)
                
            
            # grp_start.next = nxt
            first = grp_start
            cur = nxt
        return dummy.next

