#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix) - 1
        for r in range(row/2 + 1):
            col = row - r
            for c in range(r, col):
                #A (r, c) -> B(c, row - r)
                matrix[r][c] , matrix[c][row - r] = matrix[c][row - r], matrix[r][c]
                #C (row - r, row - c) -> D(row -c, r)
                matrix[row - r][row -c] , matrix[row - c][r] = matrix[row -c][r], matrix[row - r][row - c]
                #A (r, c) -> C(row -r, row -c)
                matrix[r][c] , matrix[row-r][row - c] = matrix[row -r ][row - c], matrix[r][c]
        return matrix

