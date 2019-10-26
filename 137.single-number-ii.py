#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, 32):
            cnt = 0
            for x in nums:
                cnt += (x >> i) & 0x1
            if cnt % 3:
                res |= 1 << i
        if res >= 2 << 30:
            res -= 2 << 31
        return res
# @lc code=end

