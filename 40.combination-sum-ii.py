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
        self.result = []
        self.combination(0, target, [])
        return list(self.result)

    def combination(self, i, target, elements):
        if target == 0 and elements not in self.result:
            self.result.append(elements)
            return
        if i == len(self.candidates) or target < self.candidates[i]:
            return
        _elements = elements[:]
        self.combination(i+1, target, _elements)
        _elements = elements[:]
        _elements.append(self.candidates[i])
        self.combination(i+1, target - self.candidates[i], _elements)


