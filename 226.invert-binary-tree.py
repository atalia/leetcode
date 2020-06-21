#
# @lc app=leetcode id=226 lang=python
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

# def printTree(root):
#     queue = [root]
#     while queue:
#         next_queue = []
#         while queue:
#             node = queue.pop(0)
#             if node:
#                 print(node.val)
#                 next_queue.append(node.left)
#                 next_queue.append(node.right)
#             else:
#                 print('null') 
#         queue = next_queue

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right = TreeNode(7)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)

# printTree(root)
# root = Solution().invertTree(root)
# printTree(root)



# @lc code=end

