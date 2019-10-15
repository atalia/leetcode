#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        head1 = l1
        while head1:
            stack1.append(head1.val)
            head1 = head1.next
        stack2 = []
        head2 = l2
        while head2:
            stack2.append(head2.val)
            head2 = head2.next
        head = None
        res = 0
        while stack1 or stack2:
            t = 0
            if stack1:
                val1 = stack1.pop()
                t += val1
            if stack2:
                val2 = stack2.pop()
                t += val2
            t += res
            res = t / 10
            t = t % 10
            T = ListNode(t)
            T.next = head
            head = T
        if res:
            T = ListNode(res)
            T.next = head
        return T

