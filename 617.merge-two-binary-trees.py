#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        node = None
        if not t1 and not t2:
            return node
        elif t1 and t2:
            node = TreeNode(t1.val+t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif t1:
            return t1
        else:
            return t2
        
        return node


# root1 = TreeNode(1)
# root1.left = TreeNode(3)
# root1.left.left = TreeNode(5)
# root1.right = TreeNode(2)

# root2 = TreeNode(2)
# root2.left = TreeNode(1)
# root2.left.right = TreeNode(4)
# root2.right = TreeNode(3)
# root2.right.right = TreeNode(7)
# node = Solution().mergeTrees(root1, root2)

# def treeShow(node):
#     if not node:
#         return
#     print(node.val)
#     treeShow(node.left)
#     treeShow(node.right)

# treeShow(node)

# @lc code=end

