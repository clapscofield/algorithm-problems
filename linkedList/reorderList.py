"""
Leetcode Problem
https://leetcode.com/problems/reorder-list/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #get the middle of the list - slow is the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half
        secondHalf = slow.next
        slow.next = None
        prev = None
        while secondHalf:
            aux = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = aux
        
        #merge both
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
        
