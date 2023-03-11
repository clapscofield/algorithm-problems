"""
Leetcode Problem
https://leetcode.com/problems/rotting-oranges/
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    #check if it is out of bounds or is not fresh
                    if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
                
