#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        """
        for r in range(1, len(triangle)):
            col = len(triangle[r])
            triangle[r][0] += triangle[r-1][0]  
            triangle[r][col-1] += triangle[r-1][-1]
            for c in range(1, col-1):
                triangle[r][c] = min(triangle[r-1][c-1] + triangle[r][c], triangle[r-1][c] + triangle[r][c])
        return min(triangle[-1])
        """
        dp = triangle[-1]
        row = len(triangle)
        for r in range(row-2,-1,-1):
            col = len(triangle[r])
            for c in range(col):
                dp[c] = min(dp[c] , dp[c+1]) + triangle[r][c]
        return dp[0]
