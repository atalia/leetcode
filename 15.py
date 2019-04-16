#给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。 
#
# 注意：答案中不可以包含重复的三元组。 
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
#满足要求的三元组集合为：
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]
# 
#

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        length = len(nums)
        hashmap = dict()
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        i = 0
        #print nums
        while i <= length - 2:
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1] and hashmap[nums[i]] > 1:
                i += hashmap[nums[i]] -1
                continue
            j = i + 1
            while j < length-1:
                if j > i + 1 and nums[j] == nums[j-1] and hashmap[nums[j]] > 1:
                    j += hashmap[nums[j]] - 2 if nums[i] == nums[j] else hashmap[nums[j]] - 1
                    continue
                s = -(nums[i] + nums[j])
                if s < 0 or s < nums[j]:
                    break
                #print i, j, nums[i], nums[j]
                if s in hashmap:
                    if nums[i] == nums[j] == s and hashmap[s] < 3:
                        j += 1
                        continue
                    elif nums[j] == s and hashmap[s] < 2:
                        j += 1
                        continue
                    else:
                        if len(result) == 0 or result[-1] != [nums[i], nums[j], s]:
                            result.append([nums[i], nums[j], s])
                j += 1
            i += 1
        return result