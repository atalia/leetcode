# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


if __name__ == '__main__':
    intervals = [[1,4],[5,8],[8,9]]
    #intervals = [[1,3],[2,6],[8,10],[15,18]]
    print Solution().merge(intervals)
