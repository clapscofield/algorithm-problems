"""
Leetcode Problem
https://leetcode.com/problems/container-with-most-water/
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxArea = 0

        while left < right:
            area = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
