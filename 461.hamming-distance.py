#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x ^= y
        ret = 0
        while x:
            x &= (x-1)
            ret += 1
        return ret


# @lc code=end

