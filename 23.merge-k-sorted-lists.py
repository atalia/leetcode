#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pre = head = ListNode(-1)
        size = len(lists)
        flag = True
        while flag:
            flag = False
            node = None
            del_idx = 0
            for idx in xrange(size):
                if not lists[idx]:
                    continue
                if not node:
                    node = lists[idx]
                    flag = True
                    del_idx = idx
                    continue
                if lists[idx].val < node.val:
                    node = lists[idx]
                    flag = True
                    del_idx = idx
            if node:
                head.next = node
                head = head.next
                lists[del_idx] = lists[del_idx].next
                  
        return pre.next

# lists = [[1,4,5],[1,3,4],[2,6]]
# lists = [[]]
# ret = []
# for list in lists:
#     pre = head = ListNode(-1)
#     for l in list:
#         head.next = ListNode(l)
#         head = head.next
#     ret.append(pre.next)

# ret = Solution().mergeKLists(ret)
# while ret:
#     print ret.val
#     ret = ret.next
# @lc code=end

