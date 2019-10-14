#
# @lc app=leetcode id=456 lang=python
#
# [456] 132 Pattern
#
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idx = len(nums) - 1
        if idx < 2:
            return False
        stack = []
        import sys
        second = -sys.maxint - 1
        while idx > 0:
            while stack and stack[-1] < nums[idx]:
                second = stack[-1]
                stack.pop()
            stack.append(nums[idx])
            idx -= 1
            if nums[idx] < second:
                return True
        return False
