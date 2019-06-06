# coding:utf-8

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
            print matrix[row][col]
            if target > matrix[row][col]:
                col += 1
            elif target < matrix[row][col]:
                row -= 1
            else:
                return True
        return False

if __name__ == '__main__':
    """
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    target = 25
    """
    """
    matrix = [[-1],[-1]]
    target = 0
    """
    matrix =  [[1, 3, 5, 7, 9],
               [2, 4, 6, 8, 10],
               [11, 13, 15, 17, 19],
               [12, 14, 16, 18, 20],
               [21, 22, 23, 24, 25]]
    target = -1
    print Solution().searchMatrix(matrix, target)
