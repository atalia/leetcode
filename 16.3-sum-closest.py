#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        record = dict()
        total = nums[0] + nums[1] + nums[2]
        diff = abs(total - target)
        for i in range(1, len(nums)-1):
            start = i - 1
            end = i + 1
            while start > -1 and end < len(nums):
                total_now = nums[start] + nums[end] + nums[i]
                if abs(total_now - target) < diff:
                    total = total_now
                    diff = abs(total_now-target)
                if total_now > target:
                    start -= 1
                elif total_now < target:
                    end += 1
                else:
                    return target
        return total

