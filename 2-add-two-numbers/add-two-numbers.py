# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        copy = dummy
        c = 0
        while l1 or l2 or c:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + c
            c = total // 10
            print(total , total % 10)
            dummy.val = total % 10
            if l1:
                l1 = l1.next
            if l2 :
                l2 = l2.next
            if c or l1 or l2:
                newNode = ListNode(0)
                dummy.next = newNode
                dummy= newNode
        return copy
        # Time → O(max(n, m))
        # Space → O(max(n, m))    
