"""
Leetcode Problem
https://leetcode.com/problems/decode-ways/
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        dp = { len(s): 1 }

        def decode(i):
            if i in dp: #already cache
                return dp[i]

            if s[i] == "0": #invalid
                return 0
            
            res = decode(i+1)
            #its in bound and it is valid double digit
            if (i+1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += decode(i+2)

            dp[i] = res
            return res
        
        return decode(0)

