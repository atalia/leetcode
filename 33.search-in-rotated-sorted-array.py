#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) / 2
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid
        high = left
        left = 0
        right = high
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left = high + 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

#print Solution().search([7,8,1,2,3,4,5,6], 2)
# @lc code=end

