#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head is None:
            return head

        cur_node = head
        for i in range(k):
            if not cur_node is None:
                tail = cur_node
                cur_node = cur_node.next
            else:
                return head

        next_head = tail.next if tail is not None else None

        pre_node = head
        cur_node = pre_node.next
        while cur_node != next_head:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        head.next = self.reverseKGroup(next_head, k)
        # print tail.val if tail is not None else None
        return tail
    

    
