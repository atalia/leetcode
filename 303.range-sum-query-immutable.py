#
# @lc app=leetcode id=303 lang=python
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._sum = [0 for i in range(len(nums)+1)]
        for i in xrange(1, len(self._sum)):
            self._sum[i] = self._sum[i-1] + nums[i-1] 
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum[j+1] - self._sum[i]
        
# N = NumArray([-2, 0, 3, -5, 2, -1])
# print N.sumRange(0,2)
# print N.sumRange(2,5)
# print N.sumRange(0,5)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

