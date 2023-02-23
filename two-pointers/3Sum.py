"""
Leetcode Problem
https://leetcode.com/problems/3sum/
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        s = sorted(nums)

        for index, num in enumerate(s):
            if index > 0 and s[index-1] == num:
                continue
            
            left = index + 1
            right = len(s) - 1
            while left < right:
                sums = num + s[left] + s[right]
                if sums > 0:
                    right -= 1
                elif sums < 0: 
                    left += 1
                else:
                    result.append([num, s[left], s[right]])
                    #update one pointer
                    left += 1
                    while s[left] == s[left-1] and left < right:
                        left += 1
        
        return result
            
