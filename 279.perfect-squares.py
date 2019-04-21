# coding:utf-8
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (41.46%)
# Total Accepted:    174.1K
# Total Submissions: 419.6K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        if not hasattr(self, 'dp'):
            self.dp = [i for i in xrange(n+1)]
            for i in range(1, int(sqrt(n))+1):
                self.dp[i*i] = 1
        for i in xrange(1, int(sqrt(n))+1):
            self.dp[n] = min(self.dp[n], self.numSquares(n-i*i) + 1)
        return self.dp[n]

