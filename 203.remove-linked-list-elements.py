#
# @lc app=leetcode id=203 lang=python
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tmp = ListNode(0)
        tmp.next = head
        pre = tmp
        node = head
        while node:
            if node.val == val:
                pre.next = node.next
            else:
                pre = node
        return tmp.next
# @lc code=end

