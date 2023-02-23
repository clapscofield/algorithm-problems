"""
Leetcode Problem
https://leetcode.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        allnums = {}

        for index, element in enumerate(nums):
            remain = target - element
            if remain in allnums:
                return [index, allnums[remain]]
            else:
                allnums[element] = index
