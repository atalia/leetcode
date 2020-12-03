#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        import math
        self.primes = [2]
        for i in xrange(3, n):
            for p in self.primes:
                if p * p > i:
                    self.primes.append(i)
                    break 
                if i % p == 0:
                    break
            else:
                self.primes.append(i)
        return len(self.primes)

#print Solution().countPrimes(499979)
#print Solution().countPrimes(4)
# @lc code=end

