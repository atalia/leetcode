# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

if __name__ == '__main__':
    print Solution().generateParenthesis(3)
