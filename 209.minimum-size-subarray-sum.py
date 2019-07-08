#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        i_s = 0
        i_e = 0
        size_s = len(nums)
        if size_s == 0:
            return 0
        result = size_s
        sum_s_e = nums[0]
        flag = False
        while i_s < size_s:
            # [i_s, i_e]
            while i_e < size_s - 1 and sum_s_e < s:
                i_e += 1
                sum_s_e += nums[i_e]
            if sum_s_e >= s:
                flag = True
                result = min(i_e - i_s + 1, result)
            sum_s_e -= nums[i_s]
            i_s += 1
        if not flag:
            return 0
        else:
            return result
        """
        i_s = 0
        i_e = 0
        size_s = len(nums)
        if size_s == 0:
            return 0
        result = size_s
        sum_s_e = nums[0]
        while i_s < size_s:
            # [i_s, i_e]
            while i_e < size_s - 1 and sum_s_e < s:
                i_e += 1
                sum_s_e += nums[i_e]
            if sum_s_e >= s:
                result = min(i_e - i_s + 1, result)
            if i_e == size_s - 1 and sum_s_e <= s:
                break
            sum_s_e -= nums[i_s]
            i_s += 1
        if result == size_s and sum_s_e < s:
            return 0
        else:
            return result
        
