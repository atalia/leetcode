#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        last = 0
        current = 0
        idx = 0
        while idx < len(nums):
            if idx > last:
                last = current
                cnt += 1
            current = max(current, nums[idx] + idx)
            idx += 1
        return cnt