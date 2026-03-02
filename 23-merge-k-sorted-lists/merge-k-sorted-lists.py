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
            # if next elemnt for recently poped node exist , then add that to heap
            if min_node:
                
                heappush(h,( min_node.val,id(min_node),min_node))
        return dummy.next

    #    Time Complexity

    #         Let:

    #         N = total number of nodes across all lists

    #         K = number of linked lists

    #         Heap operations

    #         Each time we:

    #         push a node into heap → O(log K)

    #         pop the smallest node → O(log K)

    #         Why log K?
    #         Because the heap size never exceeds K (at most one node per list).

    #         How many times do we do this?

    #         Every node in all lists is:

    #         inserted into heap once

    #         removed from heap once

    #         Total nodes processed = N

    #         Final Time Complexity
    #         𝑂
    #         (
    #         𝑁
    #         log
    #         ⁡
    #         𝐾
    #         )
    #         O(NlogK)

    #         because for each of the N nodes we do a heap operation.

    #         📦 Space Complexity

    #         Heap stores at most one node from each list

    #         𝑂
    #         (
    #         𝐾
    #         )
    #         O(K)
    #         ✅ Final Answer (Interview Style)

    #         Time Complexity:

    #         Each of the N nodes is pushed and popped from a heap of size K

    #         Heap operations cost log K

    #         TC
            
    #         =
            
    #         O(N
            
    #         log
            
    #         K)
    #         TC = O(N log K)

    #         Space Complexity:

    #         Heap stores at most K nodes

    #         SC
            
    #         =
            
    #         O(K)
    #         SC = O(K)