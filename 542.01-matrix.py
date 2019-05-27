#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.matrix = matrix
        self.size = len(matrix)
        self.min_distance = [[101 for m in range(self.size)] for n in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.bfs(i, j)
        return self.min_distance
        
    def bfs(self, i, j):
        if self.min_distance[i][j] < 101:
            return self.min_distance[i][j]
        if self.matrix[i][j] == 0:
            self.min_distance[i][j] = 0
            return 0
        left = 101
        right = 101
        up = 101
        down = 101
        if i - 1 > 0:
            left = 1 + self.bfs(i - 1, j)
        if i + 1 < self.size:
            right = 1 + self.bfs(i + 1, j)
        if j - 1 > 0:
            up = 1 + self.bfs(i ,j - 1)
        if j + 1 < self.size:
            down = 1 + self.bfs( i ,j + 1)
        self.min_distance[i][j] = min(left , right , up , down)
        return self.min_distance[i][j]


