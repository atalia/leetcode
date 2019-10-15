#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        res = 0
        while start < end:
            mn = min(height[start], height[end])
            if mn == height[start]:
                while start < end and mn >= height[start]:
                    res += mn - height[start]
                    start += 1
            else:
                while start < end and mn >= height[end]:
                    res += mn - height[end]
                    end -= 1
        return res


#print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
# @lc code=end

