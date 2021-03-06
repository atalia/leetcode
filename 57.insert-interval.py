#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        idx = 1
        start, end = intervals[0]
        res = []
        while idx < len(intervals):
            if intervals[idx][0] > end:
                res.append([start, end])
                start, end = intervals[idx]
            else:
                end = max(end, intervals[idx][1])
            idx += 1
        if not res:
            res.append([start, end])
        if res[-1][1] >= start:
            res[-1][1] = end
        else:
            res.append([start, end])
        return res


# intervals = [[5,6]]
# newInterval =  [4,8]
# print Solution().insert(intervals, newInterval)
# @lc code=end

