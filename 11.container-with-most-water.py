#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        vol = min(height[left], height[right]) * (right -left)
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            vol = max(vol, min(height[left], height[right]) * (right -left))
        return vol
            


