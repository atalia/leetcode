#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        heap = []
        import heapq
        for ele, cnt in nums_dict.iteritems():
            heapq.heappush(heap, (-cnt, ele))
        idx = 0
        elements = []
        while idx < k:
            _, ele = heapq.heappop(heap)
            elements.append(ele)
            idx += 1
        return elements

# @lc code=end

