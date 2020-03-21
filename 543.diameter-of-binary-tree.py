#
# @lc app=leetcode id=543 lang=python
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, root):
        if not root:
            return -1
        left = self.dfs(root.left) + 1
        right = self.dfs(root.right) + 1
        self.max = max(left + right, self.max)
        return max(left, right)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.righ = TreeNode(5)
# root.right = TreeNode(3)
# print Solution().diameterOfBinaryTree(root)

# @lc code=end

