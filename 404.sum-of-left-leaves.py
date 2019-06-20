#
# @lc app=leetcode id=404 lang=python
#
# [404] Sum of Left Leaves
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not hasattr(self, 'sum_value'):
            self.sum_value = 0
        if root is None:
            return self.sum_value
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                self.sum_value += root.left.val
            self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            self.sumOfLeftLeaves(root.right) 
        return self.sum_value

