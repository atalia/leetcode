#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end - 1:
            mid = start + (end - start)/2
            if nums[start] > nums[mid]:
                end = mid
            elif nums[end] < nums[mid]:
                start = mid
            else:
                break
        return min(nums[start], nums[end])