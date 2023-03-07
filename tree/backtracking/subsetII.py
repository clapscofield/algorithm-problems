"""
Leetcode Problem
https://leetcode.com/problems/subsets-ii/
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()

        subset = []
        nums.sort()
        def backtracking(curr):
            if curr >= len(nums): 
                res.add(tuple(subset))
                return

            #include curr
            subset.append(nums[curr])
            backtracking(curr + 1)

            #do not include curr
            subset.pop()
            backtracking(curr + 1)
        
        backtracking(0)
        return list(map(list, res))
