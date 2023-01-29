# Reverse Linked List (Easy)
# Link - https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    # def reverseList(self, head, prev=None):
    #     if not head:
    #         return prev
    #     next = head.next
    #     head.next = prev
    #     return self.reverseList(next, head)


# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
