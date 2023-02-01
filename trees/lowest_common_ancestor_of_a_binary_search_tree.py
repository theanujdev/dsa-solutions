# Lowest Common Ancestor of a Binary Search Tree (Medium)
# Link - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Given a binary search tree(BST), find the lowest common ancestor(LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants(where we allow a node to be a descendant of itself)."

# Example 1:
# Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #  iterative
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cn = root
        while cn:
            if p.val < cn.val and q.val < cn.val:
                cn = cn.left
            elif p.val > cn.val and q.val > cn.val:
                cn = cn.right
            else:
                return cn

    # recursive
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     if root.val<min(p.val,q.val):
    #        return self.lowestCommonAncestor(root.right,p,q)
    #     elif root.val>max(p.val,q.val):
    #        return self.lowestCommonAncestor(root.left,p,q)
    #     else:
    #         return root
