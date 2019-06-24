#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        a = 0
        offset = 0
        while a < len(nums):
            b = a + 1
            while b < len(nums) and nums[b] == nums[a]:
                b += 1
            cnt = b - a
            result += min(cnt, 2)
            nums[a - offset] = nums[a]
            if cnt > 1:
                nums[a - offset + 1] = nums[a]
            offset += 0 if cnt <= 2 else cnt - 2
            a = b
        return result
