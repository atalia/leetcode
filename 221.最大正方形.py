#coding:utf-8
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row_len = len(matrix)
        if row_len < 1:
            return 0
        col_len = len(matrix[0])
        if col_len < 1:
            return 0
        edge_max = 0
        
        for row in xrange(0, row_len):
            for col in xrange(0, col_len):
                if matrix[row][col] == '1':
                    matrix[row][col] = 1
                    edge_max = 1
                else: 
                    matrix[row][col] = 0
        for row in xrange(row_len-2, -1, -1):
            for col in xrange(col_len-2, -1, -1):
                if matrix[row][col] == 1:
                    matrix[row][col] = min(matrix[row+1][col], matrix[row+1][col+1], matrix[row][col+1]) + 1
                    edge_max = max(edge_max, matrix[row][col])
        return edge_max * edge_max


# @lc code=end

