# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:       
        h = []
        dummy = ListNode()
        cur = dummy
        for n in lists:
                if n  :
                    heappush(h,( n.val,id(n),n))
        
        while h:
            
           
            val, _,min_node = heappop(h)
            cur.next = min_node
            cur = min_node
            min_node = min_node.next
            
            if min_node:
                
                heappush(h,( min_node.val,id(min_node),min_node))
        return dummy.next
        