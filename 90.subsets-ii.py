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
        res = [[]]
        nums.sort()
        self._subset(nums, res)
        return list(res)

    def _subset(self, nums, res):
        if not nums:
            return
        # not add this num
        # add this num
        for r in res[:]:
            t = r[:]
            t.append(nums[0])
            if t not in res:
                res.append(t)
        self._subset(nums[1:], res)

# @lc code=end

#print Solution().subsetsWithDup([2,1,2])
