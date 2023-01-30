# Remove Nth Node From End of List (Medium)
# Link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next
