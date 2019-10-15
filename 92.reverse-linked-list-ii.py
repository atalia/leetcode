#
# @lc app=leetcode id=92 lang=python
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre_head_node = ListNode(0)
        pre_head_node.next = head
        idx = 1
        m_pre_node = pre_head_node
        while idx < m:
            m_pre_node = m_pre_node.next
            idx += 1

        m_node = m_pre_node.next
        next_node = m_node.next
        pre_node = m_node
        cur_node = m_node
        while idx < n:
            cur_node = next_node
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            idx += 1

        m_pre_node.next = cur_node
        m_node.next = next_node
        return pre_head_node.next

