#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        right = 1
        res = [1 for _ in nums]
        n = len(nums)
        for idx in xrange(n):
            res[idx] *= left
            left *= nums[idx]
            res[n-1-idx] *= right
            right *= nums[n-1-idx] 
        return res

# @lc code=end

