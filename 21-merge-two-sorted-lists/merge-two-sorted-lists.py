# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        head = dummy
        while head1 and head2:
            if head1.val < head2.val:
                temp = head1.next
                dummy.next = head1
                head1 =  temp
            else:
                temp = head2.next
                dummy.next = head2
                head2 = temp 
            dummy = dummy.next
        
        if head1:
            dummy.next = head1
        if head2:
            dummy.next = head2
        return head.next


# TC O(n + m)
# SC O(1)