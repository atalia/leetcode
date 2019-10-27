#
# @lc app=leetcode id=129 lang=python
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = []
        self.helper(root, 0)
        return sum(self.res)

    def helper(self, root, num):
        if root and not root.left and not root.right:
            self.res.append(10 * num + root.val)
            return
        if root.left:
            self.helper(root.left, 10 * num + root.val)
        if root.right:
            self.helper(root.right, 10 * num + root.val)

        
# @lc code=end

