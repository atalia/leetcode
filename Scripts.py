# coding:utf-8


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


if __name__ == "__main__":
    print Solution().maxArea([1,8,6,2,5,4,8,3,7])
