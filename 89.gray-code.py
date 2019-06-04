#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0 for _ in range(pow(2, n))]
        for i in range(pow(2,n)):
            result[i] = (i >> 1) ^ i
        return result

