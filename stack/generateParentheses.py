"""
Leetcode Problem
https://leetcode.com/problems/generate-parentheses/
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #only add open parentheses if open < n
        #only add close parentheses if close < open
        #valid answer if close == open == n

        stack = []
        res = []

        def backtracking(openN, closeN):
            if openN == closeN == n: #find result
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtracking(openN+1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN+1)
                stack.pop()

        backtracking(0,0)
        return res
            
