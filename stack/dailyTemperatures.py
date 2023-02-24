"""
Leetcode Problem
https://leetcode.com/problems/daily-temperatures/
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for index, temp in enumerate(temperatures):
            #if stack has elements and the top is bigger than the actual temp
            while stack and stack[-1][0] < temp: 
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (index - stackIndex)
            stack.append([temp, index])

        return res
