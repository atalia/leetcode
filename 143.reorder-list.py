#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        node_list = []
        cur_node = head
        while cur_node:
            node_list.append(cur_node)
            cur_node = cur_node.next
        node_size = len(node_list)
        n = 0
        cur_node = head
        while n < node_size/2:
            next_node = cur_node.next
            cur_node.next = node_list[node_size-n-1]
            node_list[node_size-n-1].next = next_node
            cur_node = next_node
            n += 1
        cur_node.next = None
