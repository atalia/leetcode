#
# @lc app=leetcode id=147 lang=python
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import sys
        dummy = ListNode(val=-sys.maxint-1)
        head
        while head:
            head_next = head.next
            dummy_node = dummy.next
            pre = dummy
            while dummy_node and dummy_node.val < head.val:
                pre = dummy_node
                dummy_node = dummy_node.next
            pre.next = head
            head.next = dummy_node
            head = head_next
        return dummy.next

# @lc code=end

