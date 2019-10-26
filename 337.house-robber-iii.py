#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.node_dict = dict()
        self.helper(root)
        return self.node_dict[root]

    def helper(self, root):
        if not root:
            return 0 
        if root in self.node_dict:
            return self.node_dict[root]
        self.helper(root.left)
        self.helper(root.right)
        val = root.val
        left, right = 0, 0
        if root.left:
            left = self.node_dict[root.left]
            val += self.helper(root.left.left) + self.helper(root.left.right)
        if root.right:
            right = self.node_dict[root.right]
            val += self.helper(root.right.left) + self.helper(root.right.right)
        self.node_dict[root] = max(val, left + right)

# @lc code=end

