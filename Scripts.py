# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack  = []
        nodes = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            nodes.append(root.val)
            root = root.right
        return nodes

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print Solution().inorderTraversal(root)
