# coding:utf-8
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (22.13%)
# Total Accepted:    250.8K
# Total Submissions: 1.1M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not hasattr(self, 'dp'):
            self.dp = [-1 for i in range(0, len(s)+1)]
            self.dp[0] = 0
        if len(s) == 1:
            if s == '0':
                self.dp[1] = 0
            else:
                self.dp[1] = 1
        if self.dp[len(s)] != -1:
            return self.dp[len(s)]
        if len(s) > 1 and s[-1] == '0':
            self.dp[len(s)] = self.dp[len(s)-1]
        if 1 <= int(s[-1]) <= 6 and 1 <= int(s[-2]) <= 2:
            self.dp[len(s)] = self.numDecodings(s[:-2]) + 2
        else:
            self.dp[len(s)]=self.numDecodings(s[:-2]) + self.numDecodings(s[-2:])
        return self.dp[len(s)]

if __name__ == '__main__':
    print Solution().numDecodings('01')
