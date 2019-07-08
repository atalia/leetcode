#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        self.board = board
        self.row = len(board)
        self.col = len(board[0])
        self.record = [[0 for c in range(self.col)] for r in range(self.row)]
        self.direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r in range(self.row):
            for c in range(self.col):
                if self.dfs(r, c, 0):
                    return True
        return False

    def dfs(self, i, j, w):
        if self.board[i][j] != self.word[w] or self.record[i][j]:
            return False
        if w == len(self.word) - 1:
            return True
        self.record[i][j] = 1
        for dr, dc in self.direction:
            if -1 < i + dr < self.row and -1 < j + dc < self.col:
                if self.dfs(i + dr, j + dc, w + 1):
                    return True
        self.record[i][j] = 0
        return False
        


