#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        neg_product = 0
        p = 1
        for num in nums:
            p *= num
            if p == 0:
                neg_product = 0
                max_product = max(0, max_product)
                p = 1
            elif p < 0:
                if neg_product == 0:
                    neg_product = p
                else:
                    max_product = max(max_product, p/neg_product)
            else:
                max_product = max(max_product, p)
        return max_product

