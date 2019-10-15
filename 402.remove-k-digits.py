#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        stack.append(num[0])
        idx = 1
        while idx < len(num):
            while k > 0 and stack and  num[idx] < stack[-1] :
                stack.pop()
                k -= 1
            stack.append(num[idx])
            idx += 1
        while k > 0 and stack:
            stack.pop()
            k -= 1
        res = ''.join(stack)
        res = res.lstrip('0')
        if not res:
            res = '0'
        return res
        