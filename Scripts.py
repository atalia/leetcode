# coding:utf-8

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur_position = 0
        zero = 0
        two = len(nums) - 1
        while cur_position < two:
            print cur_position
            if nums[cur_position] == 0:
                nums[zero], nums[cur_position] = nums[cur_position] , nums[zero]
                zero += 1
            elif nums[cur_position] == 2:
                nums[two], nums[cur_position] = nums[cur_position], nums[two]
                two -= 1
            cur_position += 1
        return nums


if __name__ == '__main__':
    nums = [0,0]
    Solution().sortColors(nums)
