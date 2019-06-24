#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        result = [str(num) for num in nums]
        result.sort(cmp= lambda x,y : cmp(x+y, y+x),reverse = True)
        return ''.join(result).lstrip('0') or '0'
        

