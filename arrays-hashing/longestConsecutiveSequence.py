"""
Leetcode Problem
https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)
        longest = 0
        leng = 0
        
        for n in nums:
            #check if it is a start of the sequence
            if (n-1) not in numsSet:
                leng = 0
                while (n + leng) in numsSet:
                    leng += 1
                longest = max(leng, longest)
        
        return longest
