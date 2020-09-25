#
# @lc app=leetcode id=557 lang=python
#
# [557] Reverse Words in a String III
#

# @lc code=start


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = 0
        s_size = len(s)
        ret = ""
        while left < s_size:
            while left < s_size and s[left] == " ":
                left += 1
            right = left
            while right < s_size and s[right] != " ":
                right += 1
            ret += self.reverseWord(s[left: right])
            if len(ret) < s_size:
                ret += " "
            left = right + 1

        return ret

    def reverseWord(self, s):
        return s[::-1]

#s = "Let's take LeetCode contest"
#print Solution().reverseWords(s)
# @lc code=end
