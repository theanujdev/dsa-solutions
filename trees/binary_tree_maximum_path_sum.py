# Binary Tree Maximum Path Sum (Hard)
# Link - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1, 2, 3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        # post order traversal of subtree rooted at 'node'

        def get_max_gain(node):
            nonlocal max_path
            if not node:
                return 0
            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            max_left = max(get_max_gain(node.left), 0)
            # add the gain / path sum from right subtree. 0 if negative
            max_right = max(get_max_gain(node.right), 0)
            current_max_path = node.val + max_left + max_right
            # set max path if got new
            max_path = max(max_path, current_max_path)
            # return the max sum for a path starting at the root of subtree
            return node.val + max(max_left, max_right)
        get_max_gain(root)
        return max_path
