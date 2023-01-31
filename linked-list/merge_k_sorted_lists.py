# Merge k Sorted Lists (Hard)
# Link - https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: The linked-lists are:
# [
#     1 -> 4 -> 5,
#     1 -> 3 -> 4,
#     2 -> 6
# ]
# merging them into one sorted list:
# 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Heap Solution, Time - O(nlogk) Space - O(n)
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode(None)
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next

    # Merge with Divide And Conquer, Time - O(nlogk) Space - O(1)
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists or len(lists) == 0:
    #         return None

    #     while len(lists) > 1:
    #         mergedLists = []
    #         for i in range(0, len(lists), 2):
    #             l1 = lists[i]
    #             l2 = lists[i + 1] if (i + 1) < len(lists) else None
    #             mergedLists.append(self.mergeList(l1, l2))
    #         lists = mergedLists
    #     return lists[0]

    # def mergeList(self, l1, l2):
    #     head = point = ListNode(0)
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             point.next = l1
    #             l1 = l1.next
    #         else:
    #             point.next = l2
    #             l2 = l1
    #             l1 = point.next.next
    #         point = point.next

    #     if not l1:
    #         point.next=l2
    #     else:
    #         point.next=l1

    #     return head.next

    # brute force, Time - O(nlogn) Space - O(n)
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     nodes = []
    #     head = point = ListNode(0)
    #     for l in lists:
    #         while l:
    #             nodes.append(l.val)
    #             l = l.next

    #     for x in sorted(nodes):
    #         point.next = ListNode(x)
    #         point = point.next

    #     return head.next
