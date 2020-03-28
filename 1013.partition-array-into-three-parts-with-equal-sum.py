#
# @lc app=leetcode id=1013 lang=python
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3:
            return False
        p = 0
        p_s = 0
        for a in A:
            p_s += a
            if p_s == s / 3:
                p_s = 0
                p += 1
        return p == 3 or p > 3 and s == 0

# @lc code=end

