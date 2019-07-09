# coding:utf-8


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


if __name__ == "__main__":
    # matrix = [
    #     [1,2],
    #     [3,4]
    # ]
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
        ]
    print Solution().rotate(matrix)
