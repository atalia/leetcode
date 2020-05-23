#coding:utf-8
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        self.string = s

        if n <= 1:
            return True
        self.deleted = False
        return self.heler(0, n-1)
    
    def heler(self, i, j):
        if i >= j:
            return True
        if self.string[i] == self.string[j]:
            return self.heler(i+1, j-1)
        elif not self.deleted:
            self.deleted = True
            return self.heler(i+1, j) or self.heler(i, j-1)
        else:
            return False
        

# @lc code=end

