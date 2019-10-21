#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        cur_node = 1
        result = []
        reverse = False
        while queue:
            next_node = 0
            layer = []
            while cur_node:
                node = queue[0]
                layer.append(node.val)
                queue.pop(0)
                cur_node -= 1
                if node.left:
                    queue.append(node.left)
                    next_node += 1
                if node.right:
                    queue.append(node.right)
                    next_node += 1
            cur_node = next_node
            if reverse:
                layer.reverse()
            reverse = not reverse
            result.append(layer)
        return result
# @lc code=end

