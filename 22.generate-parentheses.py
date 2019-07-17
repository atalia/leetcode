#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        l = n
        r = 0
        self.result  = []
        self._addParenteses('(', l-1, r+1)
        return self.result

    def _addParenteses(self, parenteses, l, r):
        if not l and not r:
            self.result.append(parenteses)
        if l:
            self._addParenteses(parenteses+'(', l-1, r+1)
        if r:
            self._addParenteses(parenteses+')', l , r-1)
        

