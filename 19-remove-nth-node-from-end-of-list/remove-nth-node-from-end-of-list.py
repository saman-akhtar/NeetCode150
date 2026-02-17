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
        # c = 0
        if cur.next:
                new_element = cur.next.next
                cur.next = new_element
         
        return head

 ## TC O(N)
 # SC O(`1`)

        
        



        # def reverseList(head:ListNode):
        #     prev = None
        #     curr = head

        #     while curr:
        #         nxt_node = curr.next
        #         curr.next = prev
        #         prev = curr

        #         curr = nxt_node
            
        #     return prev

        # def remove(head: ListNode,n):

        #     head = reverseList(head)

        #     if n == 1:
        #         head = head.next
            
        #     else:
        #         curr = head

        #         for i in range(n - 2):
        #             curr = curr.next

        #         curr.next = curr.next.next


        #     head = reverseList(head)
        #     return head

        # return remove(head, n)




    #     length = 0
    #  #   print("head", head)
    #     curr = head

    #     while curr:
            
    #         length += 1
            
    #         curr = curr.next
    #    #     print("len", length)
    #    #     print("initial curr",curr)
            
            
        
    #     pos_begin = length - n 

    #     if pos_begin == 0:
    #         return head.next

    #     curr = head

    #  #   print("current", curr)

    #     for i in range(pos_begin - 1):
    #         curr = curr.next

    #      #   print("inside curr", curr)

    #     curr.next = curr.next.next


    #  #   print( "head", head)

    #     return head




    #     # dummy = ListNode(0, head)

    #     # l = dummy
    #     # r = dummy

    #     # for _ in range(n):
    #     #     r = r.next

    #     # while r.next:
    #     #     r = r.next
    #     #     l = l.next

    #     # l.next = l.next.next

    #     # return dummy.next

        