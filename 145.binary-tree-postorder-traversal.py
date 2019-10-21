#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        pre = node
        stack = []
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is pre or not node.right:
                pre = stack.pop()
                res.append(pre.val)
                node = None
            else:
                node = node.right
        return res

# @lc code=end

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.left.right = TreeNode(6)
# root.left.right = TreeNode(5)
# root.left.right.right = TreeNode(7)
# root.right.left = TreeNode(8)
# print Solution().postorderTraversal(root)
