# Kth Smallest Element in a BST (Medium)
# Link - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Given the root of a binary search tree, and an integer k, return the kth smallest value(1-indexed) of all the values of the nodes in the tree.

# Example 1:
# Input: root = [3, 1, 4, null, 2], k = 1
# Output: 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iterative
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    # recursive
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     inorder = []
    #     def rec(node,res):
    #         if not node:
    #             return
    #         rec(node.left,res)
    #         res.append(node.val)
    #         rec(node.right,res)
    #     rec(root,inorder)
    #     return inorder[k-1]
