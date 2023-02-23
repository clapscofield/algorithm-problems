"""
Leetcode Problem
https://leetcode.com/problems/valid-anagram/
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        letters_s = {}
        for letter in s:
            letters_s[letter] = 1 + letters_s.get(letter, 0)
        
        for letter in t:
            if letter in letters_s:
                letters_s[letter] = letters_s[letter] - 1
        
        for key, value in letters_s.items():
            if value != 0:
                return False

        return True
