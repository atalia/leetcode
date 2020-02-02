#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num, cnt = nums[0], 1
        for idx in xrange(1, len(nums)):
            if nums[idx] == num:
                cnt += 1
            else:
                cnt -= 1
                if not cnt:
                    num = nums[idx]
                    cnt += 1
        return num

# @lc code=end

