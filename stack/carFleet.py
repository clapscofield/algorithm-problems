"""
Leetcode Problem
https://leetcode.com/problems/car-fleet/
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs.sort()

        stack = []
        for p, s in pairs[::-1]:  #goes in reverse order
            stack.append((target - p)/s)
            # does it overlap? must be more than 1 car
            # and the time must be less, it means it will reach the other
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() #remove the one more distant
        
        return len(stack)
