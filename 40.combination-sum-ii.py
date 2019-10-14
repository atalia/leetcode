#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = [x for x in candidates if x <= target]
        self.candidates.sort()
        idx = 0
        self.result = set()
        self.combination(0, target, [])
        return list(self.result)

    def combination(self, i, target, elements):
        if target == 0:
            self.result.add(elements)
            return
        if i == len(self.candidates):
            return
        if target < 0:
            return 
        self.combination(i+1 , target, elements)
        self.combination(i+1 , target - self.candidates[i], elements.append(self.candidates[i]))

candidates = [10,1,2,7,6,1,5] 
target = 8

Solution().combinationSum2(candidates, target)
