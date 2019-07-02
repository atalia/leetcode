#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dis = 0
        size_nums = len(nums)
        for i in range(size_nums):
            dis = max(dis, i + nums[i])
            if dis == i and i != size_nums -1:
                return False
            if dis >= size_nums -1:
                return True
        return True
        

