"""
Leetcode Problem
https://leetcode.com/problems/climbing-stairs/
"""

#Solution with Fibonacci numbers. DP bottom up. How many steps to reach the end?
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        
        for i in range(n-1):
            aux = one
            one = one + two
            two = aux
        
        return one
