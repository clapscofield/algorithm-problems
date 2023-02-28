"""
Leetcode Problem
https://leetcode.com/problems/permutation-in-string/
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sortS1 = sorted(s1)
        
        l = 0
        for r in range(len(s2)):
            if (r - l + 1) == len(s1):
                #order window caracteres and compare
                windowSort = sorted(s2[l:r+1])
                if windowSort == sortS1:
                    return True
                else:
                    l += 1
            
        return False
