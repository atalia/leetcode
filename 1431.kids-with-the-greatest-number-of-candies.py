#
# @lc app=leetcode id=1431 lang=python
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        candies_max = max(candies)
        ret = [False for _ in candies]
        for idx in xrange(len(candies)):
            if candies[idx] - candies_max + extraCandies >= 0:
                ret[idx] = True
        return ret
# @lc code=end

