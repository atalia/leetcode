# coding:utf-8

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        start_p = 0
        end_p = m * n - 1
        while start_p <= end_p:
            print start_p, end_p
            mid_p = start_p + (end_p-start_p) / 2
            mid_r = mid_p / n
            mid_c = mid_p - mid_r * n
            if matrix[mid_r][mid_c] < target:
                start_p = mid_p + 1
            elif matrix[mid_r][mid_c] > target:
                end_p = mid_p - 1
            else:
                return True
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 13
    print Solution().searchMatrix(matrix, target)
