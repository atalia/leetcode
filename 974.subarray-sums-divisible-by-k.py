#
# @lc app=leetcode id=974 lang=python
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        sum_tmp = 0
        mod_map = {0:1}
        for a in A:
            sum_tmp += a
            mod = sum_tmp % K
            if mod not in mod_map:
                mod_map[mod] = 0 
            mod_map[mod] += 1
        ret = 0
        for v in mod_map.itervalues():
            ret += v * (v - 1) / 2
        return ret

# @lc code=end

