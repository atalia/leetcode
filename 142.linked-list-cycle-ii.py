#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is head:
            return head
        first = head
        second = head
        while first is not None and second is not None:
            first = first.next
            if second.next is not None:
                second = second.next.next
            else:
                return None
            if first is second:
                break
        if not second or not first:
            return None
        first = head
        while first is not second:
            first = first.next
            second = second.next
        return first


        
        

