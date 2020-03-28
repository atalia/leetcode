#
# @lc app=leetcode id=876 lang=python
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
# def BuildList(list_node):
#     head = ListNode(0)
#     node = head
#     for l in list_node:
#         node.next = ListNode(l)
#         node = node.next
#     return head.next

# head = BuildList([1,2,3,4,5,6])

# node = Solution().middleNode(head)
# while node:
#     print node.val
#     node = node.next 
# @lc code=end

