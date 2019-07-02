#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row = len(board)
        if not self.row:
            return self.board
        self.col = len(board[0])
        self.visited = [[0 for i in range(self.col)] for j in range(self.row)]
        for c in range(self.col):
            self.dfs(0, c)
            self.dfs(self.row - 1, c)
        for r in range(self.row):
            self.dfs(r, 0)
            self.dfs(r, self.col-1)
        self.modify('O', 'X')
        self.modify('#', 'O')
        return self.board

    def dfs(self, i, j):
        if self.visited[i][j]:
            return
        self.visited[i][j] = 1
        if self.board[i][j] != 'O':
            return
        self.board[i][j] = '#'
        step = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for x, y in step:
            if 0 <= i+x < self.row and 0 <= j+y < self.col:
                self.dfs(i+x, j+y)



    def modify(self, source_chr, target_chr):
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == source_chr:
                    self.board[i][j] = target_chr

