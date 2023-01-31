# Maximum Depth of Binary Tree (Easy)
# Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l+1, r+1)

    # iterative
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     stack = [(0,root)]
    #     max_depth = 0
    #     while len(stack):
    #         depth, curr = stack.pop()
    #         max_depth = max(max_depth,depth+1)
    #         if curr.left:
    #             stack.append((depth+1,curr.left))
    #         if curr.right:
    #             stack.append((depth+1,curr.right))
    #     return max_depth
