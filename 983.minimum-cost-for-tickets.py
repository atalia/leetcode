#
# @lc app=leetcode id=983 lang=python
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        day_max = days[-1]
        dp = [0 for i in xrange(day_max+1)]
        for idx in xrange(1, day_max+1):
            if idx not in days:
                dp[idx] = dp[idx-1]
                continue
            m = min(dp[max(0, idx-1)] + costs[0], 
                dp[max(0, idx-7)] + costs[1],
                dp[max(0, idx-30)] + costs[2])
            
            dp[idx] = m
        return dp[-1]
  
# @lc code=end

