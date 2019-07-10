#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        nodes = []
        nodes.append(root)
        current_nodes = 1
        result = []
        while nodes:
            next_nodes = 0
            current = []
            while current_nodes:
                node = nodes.pop(0)
                current.append(node.val)
                current_nodes -= 1
                if node.left:
                    nodes.append(node.left)
                    next_nodes += 1
                if node.right:
                    nodes.append(node.right)
                    next_nodes += 1
            if current:
                result.append(current)
            current_nodes = next_nodes
        return result
            
