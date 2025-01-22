# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       
        def reverse(cur,  groupNext):
            prev = None
            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        def getKth(node, k):
            while node and k > 0:
                node =node.next
                k = k -1
            return node

        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kthNode = getKth(groupPrev, k)
            if not kthNode:
                break
            groupNext = kthNode.next
            cur = groupPrev.next
            newHead = reverse(cur,  groupNext)

            groupStart = groupPrev.next
            groupPrev.next = newHead
            groupStart.next = groupNext ## Connect the tail of the reversed group to the next group

            # Move groupPrev to the end of the reversed group
            groupPrev = groupStart
        return dummy.next