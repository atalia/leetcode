#
# @lc app=leetcode id=365 lang=python
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        elif z == x + y:
            return True
        else:
            return not (z % self.gcd(x, y))

    def gcd(self, x, y):
        if x < y:
            x, y = y, x
        if y:
            
            while x and y:
                x %= y
                if x:
                    y %= x
        return x + y

#print Solution().canMeasureWater(104681, 104683, 54)
#print Solution().canMeasureWater(3, 3, 4)
# @lc code=end

