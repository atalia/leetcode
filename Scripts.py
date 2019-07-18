# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(T)
        result = [0 for _ in range(n)]
        for i in xrange(n):
            while stack and T[i] > T[stack[-1]]:
                t = stack.pop()
                result[t] = i - t
            stack.append(i)
        return result




if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    #intervals = [[1,3],[2,6],[8,10],[15,18]]
    print Solution().dailyTemperatures(T)
