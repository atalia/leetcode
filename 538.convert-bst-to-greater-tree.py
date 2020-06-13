#
# @lc app=leetcode id=538 lang=python
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if not hasattr(self, "sumval"):
            self.sumval = 0
        self.convertBST(root.right)
        root.val += self.sumval
        self.sumval = root.val
        self.convertBST(root.left)
        return root

# root = TreeNode(5)
# root.left = TreeNode(2)
# root.right = TreeNode(13)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(16)
# Solution().convertBST(root)

# def treePrint(root):
#     if not root:
#         return 
#     print(root.val)
#     treePrint(root.left)
#     treePrint(root.right)
# treePrint(root)
# @lc code=end

