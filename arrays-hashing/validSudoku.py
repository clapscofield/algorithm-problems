"""
Leetcode Problem
https://leetcode.com/problems/valid-sudoku/
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #each column has a set to identify it values, to check therepeated ones
        cols = collections.defaultdict(set) #key = col index value = col values
        rows = collections.defaultdict(set)  #key = row index value = row values
        squares = collections.defaultdict(set)  #key = (row/3, col/3) value = grid values

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[r//3, c//3]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])

        return True
