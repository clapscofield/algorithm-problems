"""
Leetcode Problem
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


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
        dummy = ListNode(0, head)
        left, right = dummy, head

        #shift right until distance L to R is n
        while n > 0 and right:
            right = right.next
            n -= 1
        
        #go to the end, and left will be prev of the one we want to delete
        while right:
            left = left.next
            right = right.next
        
        #delete the node
        left.next = left.next.next

        return dummy.next

