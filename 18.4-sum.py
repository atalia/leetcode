#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_table = dict()
        sum_2_table = dict()
        for num in nums:
            if num not in nums_table:
                nums_table[num] = 0
            nums_table[num] += 1
        a = 0
        while a < len(nums) - 1:
            while a > 1 and a < len(nums) - 1 and nums[a] == nums[a-1]:
                a += 1
            if a == len(nums) -1:
                continue
            b = a + 1
            while b < len(nums):
                while b > a + 1 and b < len(nums) and nums[b] == nums[b-1]:
                    b += 1
                if b == len(nums):
                    continue
                s_t = nums[a] + nums[b]
                if s_t not in sum_2_table:
                    sum_2_table[s_t] = []
                sum_2_table[s_t] .append([nums[a], nums[b]])
                b += 1
            a += 1
        result = set()
        sum_2 = sum_2_table.keys()
        sum_2.sort()
        for k in sum_2:
            if target-k < k:
                break
            if (target - k) not in sum_2_table:
                continue
            for x in sum_2_table[k]:
                for y in sum_2_table[target-k]:
                    ret = x + y
                    if any(nums_table[i] < ret.count(i) for i in ret):
                        continue
                    else:
                        ret.sort()
                        result.add(tuple(ret))
        return list(list(r) for r in result)


        
