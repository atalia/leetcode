#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_size = len(nums)
        for idx in range(nums_size):
            elem = abs(nums[idx]) - 1
            nums[elem] = - abs(nums[elem])
        ret = []
        for idx in range(nums_size):
            if nums[idx] > 0:
                ret.append(idx+1)
        return ret

#print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
# @lc code=end

