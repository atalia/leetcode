# coding:utf-8


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dis = 0
        size_nums = len(nums)
        for i in range(size_nums):
            dis = max(dis, i + nums[i])
            if dis == i:
                return False
            if dis >= size_nums -1:
                return True
        return True

if __name__ == "__main__":
    print Solution().canJump([3,2,1,0,4])
