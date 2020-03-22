#
# @lc app=leetcode id=945 lang=python
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        A_len = len(A)
        step = 0
        for idx in xrange(1, A_len):
            if A[idx] <= A[idx-1]:
                step += A[idx-1] + 1 - A[idx]
                A[idx] = A[idx-1] + 1
        return step

#print Solution().minIncrementForUnique([1,2,2])
# @lc code=end

