#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.make_min_heap(nums)
        i = 0
        while i < k - 1:
            i += 1
            nums[0], nums[-i] = nums[-i], nums[0]
            self.down(nums, len(nums)-i)
        return nums[0]

    @staticmethod
    def make_min_heap(nums):
        parent = len(nums)/2 -1
        while parent >= 0:
            son = 2 * parent + 1
            while son < len(nums):
                if son + 1 < len(nums):
                    son = son + 1 if nums[son] < nums[son + 1] else son
                if nums[son] >= nums[(son-1)/2]:
                    nums[son], nums[(son-1)/2] = nums[(son-1)/2], nums[son]
                else:
                    break
                son = 2 * son + 1
            parent -= 1
    
    @staticmethod
    def down(nums, size):
        num = nums[0]
        parent = 0
        while 2 * parent + 1 < size:
            son = 2 * parent + 1
            if son + 1 < size and nums[son] < nums[son+1]:
                son = son + 1
            if num > nums[son]:
                break
            else:
                nums[parent] = nums[son]
            parent = son
        nums[parent] = num

# @lc code=end

