"""
Leetcode Problem
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carry = 0

        p1, p2 = l1, l2

        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            sumNumbers = carry + v1 + v2
            carry = sumNumbers // 10
            digit = sumNumbers % 10

            #insert into the list
            cur.next = ListNode(digit)
            cur = cur.next
            p1, p2 = p1.next if p1 else None, p2.next if p2 else None
    
    
        return dummy.next
