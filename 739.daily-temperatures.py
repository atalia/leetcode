#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(T)
        result = [0 for _ in range(n)]
        for i in xrange(n):
            while stack and T[i] > T[stack[-1]]:
                t = stack.pop()
                result[t] = i - t
            stack.append(i)
        return result
            

