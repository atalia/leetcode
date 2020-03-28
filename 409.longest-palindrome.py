#
# @lc app=leetcode id=409 lang=python
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_map = dict()
        for i in s:
            if i not in s_map:
                s_map[i] = 0
            s_map[i] += 1
        ret = 0
        for v in s_map.itervalues():
            ret += v / 2
        ret *= 2
        if ret  < len(s):
            ret += 1
        return ret

#print Solution().longestPalindrome("")
# @lc code=end

