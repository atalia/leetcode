#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        size = len(citations)
        i = 0
        for i in range(0, size):
            if citations[i] <= i:
                return i
        return size

