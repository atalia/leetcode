# coding:utf-8


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        root = int(sqrt(n)) + 1
        if not hasattr(self, 'dp'):
            self.dp = [i for i in xrange(n+1)]
            for i in range(1, root):
                self.dp[i*i] = 1
        if self.dp[n] == 1:
            return 1
        for i in xrange(1, n+1):
            for j in xrange(1, root):
                if i - j * j < 0:
                    break
                self.dp[i] = min(self.dp[i-j*j]+1, self.dp[i])
        return self.dp[n]

if __name__ == '__main__':
    S = Solution()
    print S.numSquares(1040)