#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        idx = 0
        while idx < len(s):
            if s[idx] != ']':
                stack.append(s[idx])
            else:
                res = []
                while stack[-1] != '[':
                    res.append(stack[-1])
                    stack.pop()
                stack.pop()
                nums = []
                while stack and stack[-1].isdigit():
                    nums.append(stack[-1])
                    stack.pop()
                stack.append(int(''.join(nums[::-1])) * ''.join(res[::-1]))
            idx += 1
        return ''.join(stack)

