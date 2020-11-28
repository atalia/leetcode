#
# @lc app=leetcode id=222 lang=python
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.getHeigh(root.left)
        right = self.getHeigh(root.right)
        if left == right:
            return pow(2, left) + self.countNodes(root.right)
        else:
            return pow(2, right) + self.countNodes(root.left)

    def getHeigh(self, root):
        if not root:
            return 0
        return 1 + self.getHeigh(root.left)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right  =TreeNode(5)
# root.right = TreeNode(3)
# root.right.left = TreeNode(6)

# print Solution().countNodes(root)
        
# @lc code=end

