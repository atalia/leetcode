# coding:utf-8


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        mid =(start + end)/ 2
        result = [-1, -1]
        while start <= end:
            mid = (start + end)/2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif mid != 0 and nums[mid - 1] != target:
                break
            else:
                end = mid - 1
        result[0] = mid if nums[mid] == target else -1
        if result[0] == -1:
            return result
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)/2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            elif mid + 1 <= len(nums) - 1 and nums[mid + 1] != target:
                break
            else:
                start = mid + 1
        result[1] = mid
        return result


if __name__ == "__main__":
    print Solution().searchRange([1,2,3], 2)
