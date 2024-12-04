# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        # reverse
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        cur = head

        # reoder
        while prev:# as in odd length second hald can be null hence check if secon list ie prev is not null , instead of ifrst half
            cnxt = cur.next
            cur.next = prev
            pnxt = prev.next
            prev.next = cnxt
            cur = cnxt
            prev = pnxt
        return head

# O(N) :