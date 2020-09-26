#
# @lc app=leetcode id=113 lang=python
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        if not root.left and not root.right:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        path = []
        if root.left:
            path +=  self.pathSum(root.left, sum - root.val)
        if root.right:
            path +=  self.pathSum(root.right, sum - root.val)
        return [[root.val] + l for l in path if path and l]
        
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.left.left = TreeNode(11)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
# root.right = TreeNode(8)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)

# print(Solution().pathSum(root, 22))
        
# @lc code=end

