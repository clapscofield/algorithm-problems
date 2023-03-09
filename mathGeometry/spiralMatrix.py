"""
Leetcode Problem
https://leetcode.com/problems/spiral-matrix/
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        while l < r and t < b:
            #left to right, in the top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1

            #right to bottom, in the right col
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and t < b):
                break

            #right to left in the bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            
            #bottom to top in the left col
            for i in range(b - 1,t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res
