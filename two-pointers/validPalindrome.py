"""
Leetcode problem
https://leetcode.com/problems/valid-palindrome/
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(c for c in s if c.isalnum())
        clean_lower = clean.lower()

        beg = 0
        end = len(clean_lower)-1
        while beg < end:
            if clean_lower[beg] != clean_lower[end]:
                return False
            beg += 1
            end -= 1

        return True
