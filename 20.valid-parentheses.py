#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        define = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if stack and stack[-1] == define[c]:
                    stack.pop(-1)
                else:
                    return False
        if not stack:
            return True
        else:
            return False
# @lc code=end

