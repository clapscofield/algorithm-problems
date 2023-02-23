"""
Leetcode Problem
https://leetcode.com/problems/contains-duplicate/
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        all_nums = {}
        for n in nums:
            if n in all_nums:
                return True
            else:
                all_nums[n] = 1
        return False
