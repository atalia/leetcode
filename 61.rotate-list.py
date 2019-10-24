#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        cnt = 0
        dummy = ListNode(0)
        dummy.next = head
        node = head
        while node.next:
            cnt += 1
            node = node.next
        cnt += 1
        k %= cnt
        k = cnt - k if k < cnt else 0

        node.next = dummy.next
        pre = node
        while k:
            pre = head
            head = head.next
            k -= 1
        dummy.next = head
        pre.next = None
        return dummy.next
# @lc code=end

# l = [1,2,3,4,5]
# head = ListNode(0)
# node = head
# for x in l:
#     node.next = ListNode(x)
#     node = node.next
#
# node = head.next
# """
# while node:
#     print node.val
#     node = node.next
# """
#
# Solution().rotateRight(head.next, 0)
#
# while head:
#     print head.val
#     head = head.next

