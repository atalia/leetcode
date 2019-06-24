#
# @lc app=leetcode id=436 lang=python
#
# [436] Find Right Interval
#
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        left_table = dict()
        i = 0
        for interval in intervals:
            left_table[interval[0]] = i
            i += 1
        left_values = left_table.keys()
        left_values.sort()
        result = [-1 for _ in range(len(left_values))]
        i = -1
        for interval in intervals:
            i += 1
            if left_table.has_key(interval[1]):
                result[i] = left_table[interval[1]]
                continue
            if left_values[-1] < interval[1]:
                continue
            else:
                left = 0
                right = len(left_values)
                while left <= right:
                    mid = left + (right - left)/2
                    if interval[1] < left_values[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
            if left_values[right] > interval[1]:
                result[i] = left_table[left_values[right]]
            else:
                result[i] = left_table[left_values[left]]
        return result

