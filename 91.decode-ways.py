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
        length = len(s) + 1
        dp = [0 for i in range(length)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in xrange(2, length):
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] = dp[i-2]
            if s[i-1] != '0':
                dp[i] += dp[i-1]
        return dp[length-1]

#print Solution().numDecodings('12')
#print Solution().numDecodings('226')
#print Solution().numDecodings('10')
#print Solution().numDecodings('0')
#print Solution().numDecodings('100')
#print Solution().numDecodings('110')
#print Solution().numDecodings('4085393587263438197362839792651187379538211951318577884164713291143976212416731331985661435443671959')

