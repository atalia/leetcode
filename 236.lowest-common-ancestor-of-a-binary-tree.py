#
# @lc app=leetcode id=236 lang=python
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
        while i<=n and p_nodes[-i] is q_nodes[-i]:
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
        

