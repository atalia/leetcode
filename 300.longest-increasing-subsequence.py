#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         nums_size = len(nums)
#         dp = [1 for _ in range(nums_size)]
#         for i in range(1, nums_size):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         return max(dp)

class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        self.dp = [nums[0]]
        for num in nums:
            if num > self.dp[-1]:
                self.dp.append(num)
            else:
                idx = self.findIndex(num)
                if self.dp[idx] < num and idx < len(self.dp) - 1:
                    idx += 1
                self.dp[idx] = num
            #print self.dp
        return len(self.dp)
    
    def findIndex(self, num):
        start = 0
        end = len(self.dp)
        while start <= end:
            mid = (start + end) / 2
            if self.dp[mid] > num:
                end = mid - 1
            elif self.dp[mid] < num:
                start = mid + 1
            else:
                break
        return mid

# s = Solution()
# s.dp = [2, 5, 6]
# print s.findIndex(4)
# print Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
# @lc code=end

