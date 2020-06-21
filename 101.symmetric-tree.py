#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.check(root.left, root.right)


    def check(self, left, right):
        if not left and not right:
            return True
        elif left and right:
            if left.val == right.val:
                return self.check(left.left, right.right) and self.check(left.right, right.left)
            else:
                return False
        else:
            return False

# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         current_quque = [root]
#         while current_quque:
#             next_queue = []
#             while current_quque:
#                 node = current_quque.pop()
#                 if node:
#                     next_queue.append(node.left)
#                     next_queue.append(node.right)
#             next_queue_size = len(next_queue)
#             for idx in range(next_queue_size/2):
#                 node_left = next_queue[idx]
#                 node_right = next_queue[next_queue_size-1-idx]
#                 if not node_left and not node_right:
#                     continue
#                 elif node_left and node_right and node_left.val == node_right.val:
#                     continue
#                 else:
#                     return False
#             current_quque = next_queue
#         return True
 
# @lc code=end
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# #root.left.right = TreeNode(4)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# #root.right.right = TreeNode(3)

#print Solution().isSymmetric(root)