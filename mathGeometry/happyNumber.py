"""
Leetcode Problem
https://leetcode.com/problems/happy-number/
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumSquares = str(n)
        sums = set()

        while sumSquares != 1:
            num = str(sumSquares)
            sumSquares = 0
            for element in num:
                sumSquares += int(element)**2

            if sumSquares in sums:
                return False
            sums.add(sumSquares)
        
        return True

