"""
Leetcode Problem
https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visit = set()
        cur = head

        while cur:
            if cur in visit:
                return True
            visit.add(cur)
            cur = cur.next
        
        return False
