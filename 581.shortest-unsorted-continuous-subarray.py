#
# @lc app=leetcode id=581 lang=python
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_back = [i for i in nums]
        nums_back.sort()
        left = 0
        while left < len(nums) and nums[left] == nums_back[left]:
            left += 1
        right = len(nums) - 1
        while right > 0 and nums[right] == nums_back[right]:
            right -= 1
        if right > left:
            return right - left + 1
        else:
            return 0

print Solution().findUnsortedSubarray([1,2])
# @lc code=end

