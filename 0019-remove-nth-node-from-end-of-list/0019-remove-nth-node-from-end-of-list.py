# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr1 = ptr2 = head
        
        for _ in range(n):
            ptr1 = ptr1.next
            
        if not ptr1: 
            return head.next
        
        while ptr1.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        ptr2.next = ptr2.next.next
        
        return head
            
            