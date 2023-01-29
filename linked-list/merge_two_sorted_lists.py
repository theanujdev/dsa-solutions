# Reverse Linked List (Easy)
# Link - https://leetcode.com/problems/merge-two-sorted-lists/

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1, 2, 4], list2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

    # def mergeTwoLists(self, list1, list2):
    #     if not list1 or not list2:
    #         return list1 or list2
    #     if list1.val < list2.val:
    #         list1.next = self.mergeTwoLists(list1.next, list2)
    #         return list1
    #     else:
    #         list2.next = self.mergeTwoLists(list1, list2.next)
    #         return list2


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
