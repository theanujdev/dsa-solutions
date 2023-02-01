# Binary Tree Level Order Traversal (Medium)
# Link - https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [9, 20], [15, 7]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iterative
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

    # recursive
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     res = []
    #     def dfs(node,level):
    #         if not node:
    #             return
    #         if len(res) < level + 1:
    #             res.append([])
    #         res[level].append(node.val)
    #         dfs(node.left, level + 1)
    #         dfs(node.right, level + 1)
    #     dfs(root,0)
    #     return res
