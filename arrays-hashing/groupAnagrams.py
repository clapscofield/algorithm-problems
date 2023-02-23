"""
Leetcode Problem
https://leetcode.com/problems/group-anagrams/
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_anagrams = {}
        # The keys for the string are their anagram sorted.
        # When sorted, all anagrams are equal.
        # aet = ["eat", "tea"] 
        result = []

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in sorted_anagrams:
                sorted_anagrams[s_sorted].append(s)
            else:
                sorted_anagrams[s_sorted] = [s]

        for key, value in sorted_anagrams.items():
            result.append(value)

        return result
