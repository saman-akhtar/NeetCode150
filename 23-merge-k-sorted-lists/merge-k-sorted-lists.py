# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        if not list:
            return []
        heap = []
        dummy = ListNode() 
        head = dummy
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val,id(node),node))
        while heap:
            
            if heap:
                node_val, nodeid, node= heapq.heappop(heap)
                nxt = node.next
                head.next = ListNode(node_val)
                head = head.next
                node = nxt
                if node:
                    heapq.heappush(heap, ( node.val,id(node),node))
                # heap.append(cur)
        return dummy.next
#         Time Complexity: O(N log k)

# Space Complexity: O(k)
        