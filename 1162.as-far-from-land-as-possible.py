#
# @lc app=leetcode id=1162 lang=python
#
# [1162] As Far from Land as Possible
#

# @lc code=start
class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.land = []
        self.sea = 0
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        for r in xrange(self.row_len):
            for c in xrange(self.col_len):
                if grid[r][c] == 1:
                    self.land.append((r,c))
                else:
                    self.sea += 1
        if not self.land or not self.sea:
            return -1
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
        distance = -1
        while self.land:
            next = []
            while self.land:
                (r, c) = self.land.pop()
                for i ,j in direction:
                    if 0 <= r + i < self.row_len and 0 <= c + j < self.col_len and grid[r+i][c+j] == 0:
                        grid[r+i][c+j] = 1
                        self.sea -= 1
                        next.append((r+i, c+j))
            distance += 1
            self.land = next
        return distance

#print Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
    # @lc code=end

