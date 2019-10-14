#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.container = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.container.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.container:
            return
        if self.min[-1] == self.container[-1]:
            self.min.pop()
        self.container.pop()
        

        

    def top(self):
        """
        :rtype: int
        """
        return self.container[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

