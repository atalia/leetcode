#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total, balance , start= 0, 0, 0
        for idx in range(len(gas)):
            balance += gas[idx] - cost[idx]
            total += gas[idx] - cost[idx]
            if balance < 0:
                start = idx + 1
                balance = 0
        return -1 if total < 0 else start
            

        
# @lc code=end

