#
# @lc app=leetcode id=961 lang=python
#
# [961] N-Repeated Element in Size 2N Array
#
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        idx = 0
        size = len(A)
        while idx < size:
            if idx + 1 < size and A[idx] == A[idx+1]:
                return A[idx]
            if idx + 2 < size and A[idx] == A[idx+2]:
                return A[idx]
            if idx + 3 < size and A[idx] == A[idx+3]:
                return A[idx]
            idx += 1

