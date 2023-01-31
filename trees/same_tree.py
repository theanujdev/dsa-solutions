# Same Tree (Easy)
# Link - https://leetcode.com/problems/same-tree/

# Given the roots of two binary trees p and q, write a function to check if they are the same or not .

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1, 2, 3], q = [1, 2, 3]
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    # iterative
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     stack = [(p, q)]
    #     while len(stack):
    #         first, second = stack.pop()
    #         if not first and not second: pass
    #         elif not first or not second: return False
    #         else:
    #             if first.val != second.val: return False
    #             stack.append((first.left, second.left))
    #             stack.append((first.right, second.right))
    #     return True
