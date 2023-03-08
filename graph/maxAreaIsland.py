"""
Leetcode Problem
https://leetcode.com/problems/max-area-of-island/
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        maxArea = 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def countArea(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or (r,c) in visited or grid[r][c] == 0):
                return 0
            visited.add((r,c))
            return (1 + countArea(r + 1, c) + countArea(r - 1, c) + countArea(r, c + 1) + countArea(r, c - 1))
            

        for r in range(rows):
            for c in range(cols):
                maxArea = max(maxArea, countArea(r,c))
        return maxArea
