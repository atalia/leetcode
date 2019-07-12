# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self._isValidBST(root, - sys.maxint + 1, sys.maxint)

    def _isValidBST(self, root ,min_val, max_val):
        if not root:
            return True
        if not min_val < root.val < max_val:
            return False
        return self._isValidBST(root.left, min_val, root.val) and self._isValidBST(root.right, root.val, max_val)

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(7)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    print Solution().isValidBST(root)
