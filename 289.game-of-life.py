#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return board
        col = len(board[0])
        if col == 0:
            return board
        neighbors = ((-1,1), (-1,0), (-1,-1), (0,1), (0,-1), (1, 1), (1, 0), (1, -1))
        for r in xrange(row):
            for c in xrange(col):
                board[r][c] <<= 1
        for r in xrange(row):
            for c in xrange(col):
                lived = 0
                for dr, dc in neighbors:
                    if 0 <= r + dr < row and 0 <= c + dc < col:
                        lived += board[r+dr][c+dc] >> 1
                
                if not board[r][c] & 0x2 and lived == 3:
                    board[r][c] = 1
                elif board[r][c] & 0x2 and 1 <lived <4:
                    board[r][c] = 3
        

        for r in xrange(row):
            for c in xrange(col):
                board[r][c] &= 0x01

# @lc code=end

