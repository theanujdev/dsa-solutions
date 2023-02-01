# Validate Binary Search Tree (Medium)
# Link - https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree(BST).

# A valid BST is defined as follows:

# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: root = [2, 1, 3]
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive Traversal with Valid Range
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if not (node.val < high and node.val > low):
                return False
            # The left and right subtree must also be valid.
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        return validate(root, float('-inf'), float('inf'))

    # Iterative Traversal with Valid Range
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     stack = [(root, -float('inf'), float('inf'))]
    #     while len(stack):
    #         node, left, right = stack.pop()
    #         if node.val <= left or node.val >= right:
    #             return False
    #         if node.left:
    #             stack.append((node.left, left, node.val))
    #         if node.right:
    #             stack.append((node.right, node.val, right))
    #     return True

    # Recursive Inorder Traversal
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def inorder(root):
    #         if not root:
    #             return True
    #         if not inorder(root.left):
    #             return False
    #         if root.val <= self.prev:
    #             return False
    #         self.prev = root.val
    #         return inorder(root.right)
    #     self.prev = -math.inf
    #     return inorder(root)

    # Iterative Inorder Traversal
    # def isValidBST(self, root: TreeNode) -> bool:
    #     stack, prev = [], -math.inf
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         # If next element in inorder traversal
    #         # is smaller than the previous one
    #         # that's not BST.
    #         if root.val <= prev:
    #             return False
    #         prev = root.val
    #         root = root.right
    #     return True
