#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return nums
        j = i - 1
        while i < len(nums) - 1 and nums[i + 1] > nums[j]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
        i = len(nums) - 1
        while j < i:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j += 1
        return nums


