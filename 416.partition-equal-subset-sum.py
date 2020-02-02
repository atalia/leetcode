#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s & 0x01:
            return False
        s = s / 2
        dp = [False for _ in xrange(s+1)]
        dp[0] = True
        for num in nums:
            for i in range(s, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[-1]

# @lc code=end

