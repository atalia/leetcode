#
# @lc app=leetcode id=659 lang=python
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        end_list = []
        list_count = []
        for num in nums:
            while end_list and end_list[0] < num-1:
                    if list_count[0] > 2:
                        end_list.pop(0)
                        list_count.pop(0)
                    else:
                        return False
            if not end_list or num-1 != end_list[0]:
                end_list.append(num)
                list_count.append(1)
            else:
                for i in xrange(len(end_list) - 1, -1, -1):
                    if num - 1 == end_list[i]:
                        end_list[i] = num
                        list_count[i] += 1
                        break
            #print end_list, list_count
        return all(lc > 2 for lc in list_count)

#print Solution().isPossible([1,2,3,4,4,5])            
# @lc code=end

