"""
Leetcode Problem
https://leetcode.com/problems/plus-one/
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #get the digits, turn into int
        num = 0
        count = 0
        for d in range(len(digits) - 1, -1, -1):
            num += digits[d] * (10**count)
            count += 1

        #sum 1
        num += 1
        
        #return the digits as arraynum += 1
        res = []
        strinnum = str(num)
        for s in strinnum:
            res.append(int(s))
        
        return res
