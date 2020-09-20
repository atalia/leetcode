#
# @lc app=leetcode id=922 lang=python
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left = 0
        right = 1
        while right < len(A):
            while left < len(A) and A[left] & 0x01 == 0x00:
                left += 2
            while right < len(A) and A[right] & 0x01 == 0x01:
                right += 2
            if left < len(A) and right < len(A):
                A[left], A[right] = A[right], A[left]
        return A

#print Solution().sortArrayByParityII([2,3,1,1,4,0,0,4,3,3])
#print Solution().sortArrayByParityII([4,2,5,7])
# @lc code=end

