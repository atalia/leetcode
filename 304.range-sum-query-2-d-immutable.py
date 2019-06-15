#
# @lc app=leetcode id=304 lang=python
#
# [304] Range Sum Query 2D - Immutable
#
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0:
                    self.matrix[i][j] += self.matrix[i-1][j] + self.matrix[i][j-1] - self.matrix[i-1][j-1]
                elif i > 0:
                    self.matrix[i][j] += self.matrix[i-1][j]
                elif j > 0:
                    self.matrix[i][j] += self.matrix[i][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > 0 and col1 > 0:
            row1 -= 1
            col1 -= 1
            return self.matrix[row2][col2] + self.matrix[row1][col1] - self.matrix[row1][col2] - self.matrix[row2][col1]
        elif row1 > 0: # col1 == 0
            row1 -= 1
            return self.matrix[row2][col2] - self.matrix[row1][col2]
        elif col1 > 0: # row1 == 0
            col1 -= 1
            return self.matrix[row2][col2] - self.matrix[row2][col1]
        else:
            return self.matrix[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

