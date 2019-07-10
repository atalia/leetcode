# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return [[]]
        nodes = []
        nodes.append(root)
        current_nodes = 1
        result = []
        while nodes:
            next_nodes = 0
            current = []
            while current_nodes:
                node = nodes.pop(0)
                current.append(node.val)
                current_nodes -= 1
                if node.left:
                    nodes.append(node.left)
                    next_nodes += 1
                if node.right:
                    nodes.append(node.right)
                    next_nodes += 1
            if current:
                result.append(current)
            current_nodes = next_nodes
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    print Solution().levelOrder(root)
