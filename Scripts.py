# coding:utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = postorder[-1]
        pos = inorder.index(root)
        root = TreeNode(root)
        root.left = self.buildTree(inorder[0:pos], postorder[0:pos])
        root.right = self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root


def print_tree(root):
    if not root:
        return
    print root.val
    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    print_tree(root)
