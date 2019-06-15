# coding:utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        queue = [root]
        cur_lay_cnt = 1
        result = []
        while queue:
            result.append(queue[-1].val)
            lay_cnt = 0
            while cur_lay_cnt:
                r = queue.pop(0)
                if r.left is not None:
                    lay_cnt += 1
                    queue.append(r.left)
                if r.right is not None:
                    lay_cnt += 1
                    queue.append(r.right)
                cur_lay_cnt -= 1
            cur_lay_cnt = lay_cnt
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print Solution().rightSideView(root)
