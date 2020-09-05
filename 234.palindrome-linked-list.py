#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        if not head or not head.next:
            return True
        if not head.next.next:
            return head.val == head.next.val
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        right = revert(fast)
        left = head
        while right and left.val == right.val:
            left = left.next
            right = right.next
        return not right
            
    
def revert(node):
    pre = None
    cur = node
    nex = cur.next
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    return pre

def debug(node):
    while node:
        print node.val,
        node = node.next
    print "\n"

# node = ListNode(1)
# node.next = ListNode(0)
# node.next.next = ListNode(1)

# print Solution().isPalindrome(node)
# @lc code=end

