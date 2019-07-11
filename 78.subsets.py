#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        sub = self.subsets(nums[1:])
        now = []
        for s in sub:
            now.append(s[:])
            s.append(nums[0])
            now.append(s)
        return now

