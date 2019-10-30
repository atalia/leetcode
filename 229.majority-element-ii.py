#
# @lc app=leetcode id=229 lang=python
#
# [229] Majority Element II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first , second, cnt_first, cnt_second = 0,0,0,0
        for num in nums:
            if first == num:
                cnt_first += 1
            elif second == num:
                cnt_second += 1
            elif cnt_first == 0:
                cnt_first = 1
                first = num
            elif cnt_second == 0:
                cnt_second = 1
                second = num
            else:
                cnt_first -= 1
                cnt_second -= 1
        cnt_first = 0
        cnt_second = 0
        for num in nums:
            if num == first:
                cnt_first += 1
            if num == second:
                cnt_second += 1
        res = set()
        if cnt_first > len(nums)/3:
            res.add(first)
        if cnt_second > len(nums)/3:
            res.add(second)
        return list(res)

# @lc code=end

