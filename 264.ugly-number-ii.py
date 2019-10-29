#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        heap = [1]
        idx = 0
        while idx < n:
            x = heapq.heappop(heap)
            while heap and heap[0] == x:
                heapq.heappop(heap)
            heapq.heappush(heap, 2 * x)
            heapq.heappush(heap, 3 * x)
            heapq.heappush(heap, 5 * x)
            idx += 1
        return x

# @lc code=end

