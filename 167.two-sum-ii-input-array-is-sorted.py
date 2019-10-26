#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            while i < j and numbers[i] + numbers[j] < target:
                i += 1
            while i < j and numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] == target:
                break
        return [i+1,j+1]
# @lc code=end
