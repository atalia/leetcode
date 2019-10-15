#
# @lc app=leetcode id=869 lang=python
#
# [869] Reordered Power of 2
#
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        idx = 0
        p = 1
        T = [[1]]
        res = self._int_to_list(N)
        cur_list = []
        while 1 <= p <= 10**9 and len(cur_list) <= len(res) :
            p <<= 1
            cur_list = self._int_to_list(p)
            T.append(cur_list)
        return res in T
            
    
    def _int_to_list(self, num):
        l = list()
        while(num > 0):
            l.append(num%10)
            num /= 10
        l.sort()
        return l

