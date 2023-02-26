"""
Leetcode problem
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        begin = 0
        word = set()

        for end in range(len(s)):
            while s[end] in word:
                word.remove(s[begin])
                begin += 1
            word.add(s[end])
            longest = max(longest, end - begin + 1)
    
        return longest
