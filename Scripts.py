# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p_found = False
        self.p = p
        self.q_found = False
        self.q = q
        self._dfs(root)
        p_nodes = []
        while p is not root:
            p_nodes.append(p)
            p = p.root
        p_nodes.append(root)
        q_nodes = []
        while q is not root:
            q_nodes.append(q)
            q = q.root
        q_nodes.append(root)
        i = 1
        n = min(len(p_nodes), len(q_nodes))
        while i <=n and p_nodes[-i] is q_nodes[-i]:
            i += 1
        i -= 1
        return p_nodes[-i]

    def _dfs(self, root):
        if not root or (self.p_found and self.q_found):
            return
        if root is self.p:
            self.p_found = True
        elif root is self.q:
            self.q_found = True
        if root.left:
            root.left.root = root
            self._dfs(root.left)
        if root.right:
            root.right.root = root
            self._dfs(root.right)

if __name__ == '__main__':
    node_3 = TreeNode(3)
    root = node_3
    node_5 = TreeNode(5)
    root.left = node_5
    node_1 = TreeNode(1)
    root.right = node_1
    node_6 = TreeNode(6)
    root.left.left = node_6
    node_2 = TreeNode(2)
    root.left.right = node_2
    node_7 = TreeNode(7)
    node_4 = TreeNode(4)
    root.left.right.left = node_7
    root.left.right.right = node_4
    node_0 = TreeNode(0)
    root.right.left = node_0
    node_8 = TreeNode(8)
    root.right.right = node_8

    print Solution().lowestCommonAncestor(root, node_5, node_4)
