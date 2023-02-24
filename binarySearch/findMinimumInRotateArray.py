"""
Leetcode Problem
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #check if it is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            else: #not sorted
                mid = (l + r) // 2
                res = min(nums[mid], res)
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

        return res
