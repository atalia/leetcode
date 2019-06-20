# coding:utf-8

        

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        reach = nums[0]
        for i in range(1, size):
            if reach < i or reach >=size-1:
                break
            else:
                reach = max(reach,i + nums[i])
        return reach >= size-1

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print Solution().canJump(nums)