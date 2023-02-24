"""
Leetcode Problem
https://leetcode.com/problems/valid-parentheses/
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        queue = []
        if len(s) == 0 or len(s) == 1:
            return False
        for i in s:
            if i=="(" or i =="[" or i=="{":
                queue.append(i)
            elif len(queue) == 0 or bracets[queue.pop()] != i:
                return False
        
        return len(queue) == 0
