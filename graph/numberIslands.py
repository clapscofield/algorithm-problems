"""
Leetcode Problem
https://leetcode.com/problems/number-of-islands/
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                #check directions up, right, left, down
                directions = [[0,1], [1,0], [-1, 0], [0, -1]]
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if ((r,c) not in visit and
                        r in range(rows) and c in range(cols)
                        and grid[r][c] == "1"):
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c) #check the adjacent "1"
                    islands += 1
        
        return islands

