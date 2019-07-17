#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or not intervals[0]:
            return intervals
        #intervals.sort(cmp=lambda x,y: -1 if x[0] < y[0] or x[0] == y[0] and x[1] < y[1] else 0)
        intervals.sort()
        now = intervals[0]
        result = []
        print intervals
        for interval in intervals:
            if interval[0] <= now[1]:
                if interval[1] <= now[1]:
                    continue
                else:
                    now[1] = interval[1]
            else:
                result.append(now)
                now = interval
        result.append(now)
        return result


