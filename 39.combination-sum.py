#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.result = []
        self._combination([], target)
        return self.result

    def _combination(self, nums, target):
        if target == 0:
            nums.sort()
            if nums not in self.result:
                self.result.append(nums)
            return
        if target < 0:
            return
        for x in self.candidates:
            self._combination(nums + [x], target - x)

