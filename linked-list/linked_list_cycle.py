# Linked List Cycle (Easy)
# Link - https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node(0-indexed).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    #  def hasCycle(self, head) -> bool:
    #     hashmap = {}
    #     while head:
    #         if head in hashmap:
    #             return True
    #         else:
    #             hashmap[head]= True
    #         head = head.next
    #     return False


# Input: head = [3, 2, 0, -4], pos = 1
# Output: true
