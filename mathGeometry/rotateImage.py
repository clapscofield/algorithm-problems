"""
Leetcode Problem
https://leetcode.com/problems/rotate-image/
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0 , len(matrix[0]) - 1
        
        while l < r:
            for i in range(r - l):
                t, b = l, r
                aux = matrix[t][l + i]
                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r -  i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = aux
            
            r -= 1
            l += 1

        return matrix
