"""
Leetcode Problem
https://leetcode.com/problems/subsets/submissions/
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        subset = []
        def dfs(curr):
            if curr >= len(nums):
                res.append(list(subset))
                return

            #decision to include [nums[curr]]
            subset.append(nums[curr])
            dfs(curr + 1)

            #decision to not include [nums[curr]]
            subset.pop()
            dfs(curr + 1)

        dfs(0)
        return res
