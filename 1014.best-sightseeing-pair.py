#
# @lc app=leetcode id=1014 lang=python
#
# [1014] Best Sightseeing Pair
#
class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        start = 0
        end = len(A) - 1
        tmp = [0 for _ in A]
        tmp[0] = A[0] + 0
        res = 0
        for i in xrange(1, len(A)):
            tmp[i] = max(A[i-1] + i - 1, tmp[i-1])
        
        for i in xrange(1, len(A)):
            res = max(res, A[i] - i + tmp[i])
        return res

