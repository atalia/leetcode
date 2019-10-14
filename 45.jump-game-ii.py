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
        cur_idx = 0
        next_idx = 0
        while next_idx < len(nums) - 1:
            delta = 1
            while cur_idx < len(nums) and delta <= nums[cur_idx]:
                if cur_idx + delta + nums[cur_idx + delta] > next_idx:
                    next_idx = cur_idx + delta
                if next_idx >= len(nums) - 1:
                    break
                delta += 1
            cur_idx = next_idx
            cnt += 1
        return cnt

nums = [2,3,1,1,4]
print Solution().jump(nums)