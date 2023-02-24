"""
Leetcode Problem
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        #Search which row contains the target
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else: 
                break
        
        #None of the rows contains the value
        if not (top <= bot):
            return False
        
        #mid will be the row that i want
        row = (top + bot) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else: 
                return True

        return False
        
