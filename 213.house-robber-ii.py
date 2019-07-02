#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]) , self._rob(nums[0:-1]))

    def _rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums) + 1)]
        dp[1] = nums[1]
        for i in range(1, len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]
        
