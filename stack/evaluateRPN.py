"""
Leetcode Problem
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numbers = []
        ops = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: x - y,
            '*' : lambda x, y: x * y,
            '/' : lambda x, y: x / y
        }

        for n in tokens:
            if n == "/" or n == "*" or n == "+" or n == "-":
                element1 = numbers.pop()
                element2 = numbers.pop()
                operation = ops[n](element2,element1)
                numbers.append(int(operation))
            else:
                numbers.append(float(n))
            
        return int(numbers.pop())
