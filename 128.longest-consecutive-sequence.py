#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set()
        for num in nums:
            nums_set.add(num)
        max_cnt = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            else:
                i = 1
                while num+i in nums:
                    i += 1
                max_cnt = max(max_cnt, i)
        return max_cnt
