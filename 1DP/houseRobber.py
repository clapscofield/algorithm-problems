"""
Leetcode Problem
https://leetcode.com/problems/house-robber/
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        for i in range(len(nums)):
            dp[i] = 0

        dp[len(nums)-1] = nums[len(nums) - 1]
        dp[len(nums)-2] = max(nums[len(nums) - 1], nums[len(nums) - 2])

        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]
