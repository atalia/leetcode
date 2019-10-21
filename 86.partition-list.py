#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next:
            if pre.next.val >= x:
                break
            pre = pre.next
        x_node = pre.next
        cur = pre
        while cur:
            if cur.next and cur.next.val < x:
                tmp = cur.next
                cur.next = cur.next.next
                tmp.next = x_node
                pre.next = tmp
                pre = pre.next
            else:
                cur = cur.next
        return dummy.next

# @lc code=end



