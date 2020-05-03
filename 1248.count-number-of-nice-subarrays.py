#
# @lc app=leetcode id=1248 lang=python
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = 0
        count = 0
        oddCnt = 0
        while right < len(nums):
            if nums[right] & 0x01 == 1:
                oddCnt += 1
            right += 1
            if oddCnt == k:
                tmp = right
                while right < len(nums) and nums[right] & 0x01 !=1:
                    right += 1
                rightCnt = right - tmp
                leftCnt = 0
                while nums[left] & 0x01 != 1:
                    left += 1
                    leftCnt += 1
                count += (leftCnt+1) * (rightCnt+1)
                left += 1
                oddCnt -= 1
        return count


# @lc code=end

