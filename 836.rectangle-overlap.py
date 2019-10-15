#
# @lc app=leetcode id=836 lang=python
#
# [836] Rectangle Overlap
#
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2

