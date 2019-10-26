#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        val_d = dict()
        while node:
            if node.val not in val_d:
                val_d[node.val] = 0
            val_d[node.val] += 1
            node = node.next
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next:
            if val_d[head.next.val] > 1:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

# root = ListNode(0)
# aa = [1,2,3,3,4,4,5]
# head = root
# for a in aa:
#     head.next =  ListNode(a)
#     head = head.next
# head = Solution().deleteDuplicates(root.next)
# while head:
#     print head.val
#     head = head.next
# @lc code=end

