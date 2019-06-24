#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row_num = len(matrix)
        col_num = len(matrix[0])
        row = row_num - 1
        col = 0
        while 0 <= row < row_num and 0 <= col < col_num:
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
        return False
