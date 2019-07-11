#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack  = []
        nodes = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nodes.append(root.val)
            root = root.right
        return nodes

