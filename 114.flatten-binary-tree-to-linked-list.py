#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        node = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = node
