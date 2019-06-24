#
# @lc app=leetcode id=106 lang=python
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = postorder[-1]
        pos = inorder.index(root)
        root = TreeNode(root)
        root.left = self.buildTree(inorder[0:pos], postorder[0:pos])
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root

