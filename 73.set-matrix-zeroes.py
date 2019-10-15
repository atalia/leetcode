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
        m = set()
        n = set()
        row = len(matrix)
        col = matrix[0]
        for r in range(row):
            for c in range(col):
                if not matrix[r][c]:
                    m.add(r)
                    n.add(c)
        for r in range(row):
            for c in range(col):
                if r in m or c in n:
                    matrix[r][c] = 0
# @lc code=end

