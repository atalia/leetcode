#
# @lc app=leetcode id=1232 lang=python
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <=2:
            return True
        base_x, base_y = coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        if base_x == 0:
            # delta(x)= 0
            for idx in xrange(1, len(coordinates)):
                if coordinates[idx][0] != coordinates[0][0]:
                    return False
            else:
                return True
        else:
            slope = base_y * 1.0 / base_x
            for idx in xrange(1, len(coordinates)):
                x, y = coordinates[idx][0], coordinates[idx][1]
                if y != coordinates[0][1] + slope * (x - coordinates[0][0]):
                    print  coordinates[0][1] + slope * (x - coordinates[0][0])
                    return False
            else:
                return True


#print Solution().checkStraightLine([[2,1],[4,2],[6,3]])
# @lc code=end

