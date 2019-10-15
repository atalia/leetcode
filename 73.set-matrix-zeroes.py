#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        firstrowzero = False
        firstcolzero = False
        row = len(matrix)
        col = len(matrix[0])
        for r in range(0, row):
            if not matrix[r][0]:
                firstrowzero = True
                break
        for c in range(0, col):
            if not matrix[0][c]:
                firstcolzero = True
                break
        for r in range(1, row):
            for c in range(1, col):
                if not matrix[r][c]:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, row):
            if not matrix[r][0]:
                for c in range(1, col):
                    matrix[r][c] = 0
        for c in range(1, col):
            if not matrix[0][c]:
                for r in range(1, row):
                    matrix[r][c] = 0
        if firstrowzero:
            for r in range(0, row):
                matrix[r][0] = 0
        if firstcolzero:
            for c in range(0, col):
                matrix[0][c] = 0

# @lc code=end

