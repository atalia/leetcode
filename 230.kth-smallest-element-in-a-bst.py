#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        stack.append(root)
        while stack:
            while node and node.left:
                node = node.left
                stack.append(node)
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                node = node.right
                stack.append(node)
            else:
                node = None

# @lc code=end

