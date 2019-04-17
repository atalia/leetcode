# coding: utf-8
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (35.26%)
# Total Accepted:    133.7K
# Total Submissions: 379.3K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.Tree(1,n)
    
    def Tree(self, start, end):
        if start > end:
            return [None]
        result = []
        for i in xrange(start, end+1):
            leftTree = self.Tree(start, i-1)
            rightTree = self.Tree(i+1, end)
            for l in leftTree:
                for r in rightTree:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result

if __name__ == '__main__':
    print Solution().generateTrees(0)