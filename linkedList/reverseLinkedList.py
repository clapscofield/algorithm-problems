"""
Leetcode problem
https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head

        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        
        return prev
