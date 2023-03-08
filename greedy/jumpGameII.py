"""
Leetcode Problem
https://leetcode.com/problems/jump-game-ii/
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goalStep = {}
        goalStep[len(nums)-1] = 0

        #goal = len(nums) - 1
        for i in range(len(nums) - 2, -1,  -1):
            n = nums[i]
            while n > 0:
                pos = i + n
                if pos in goalStep:
                    goalStep[i] = min(goalStep[pos] + 1, goalStep.get(i, 100000000))
                n -= 1
        
        return goalStep[0]
