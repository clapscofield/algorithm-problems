"""
Leetcode Problem
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() #for already visited cells
        res = []

        def dfs(r, c, visit, prevHeight):
            #check if is out of bounds, if it is already in visit or if it 
            # cannot flow water 
            if ((r,c) in visit or r == rows or c == cols or r < 0 or c < 0
                or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols):
            #Pacific ocean row 0 and goes to each column TOP edge
            dfs(0, c, pac, heights[0][c])
            #Atlantic ocean rows - 1 and goes to each column BOTTOM edge
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            #Pacific ocean column 0 and goes to each row LEFT edge
            dfs(r, 0, pac, heights[r][0])
            #Atlantic ocean column - 1 and goes to each row RIGHT edge
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        #check the cells that goes to both oceans
        for r in range(rows):
            for c in range(cols):
                if ((r,c) in pac and (r,c) in atl):
                    res.append([r,c])
        
        return res


            
