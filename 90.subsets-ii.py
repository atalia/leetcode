#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = ()
        self._subset(nums, res)
        return res

    def _subset(self, nums, res):
        if not nums:
            return
        # not add this num
        self._subset(nums[1:], res)
        # add this num
        for r in res:
            res.add( r.append(nums[0]))
        self._subset(nums[1:], res)
# @lc code=end

