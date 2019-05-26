#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        new_head = head.next
        pre = ListNode(0)
        pre.next = head
        while head and head.next:
            pre.next = head.next
            head.next = pre.next.next
            pre.next.next = head
            pre = head
            head = head.next
        return new_head

