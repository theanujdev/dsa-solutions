# Path Sum (Easy)
# Link - https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Example 1:
# Input: root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs recusion
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sum):
            if not node:
                return
            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum
            return dfs(node.left, sum) or dfs(node.right, sum)
        return dfs(root, 0)

    # dfs iterative
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     stack = [(root, sum)]
    #     while stack:
    #         node, curr_sum = stack.pop()
    #         if not node:
    #             continue
    #         if not node.left and not node.right:
    #             return curr_sum == node.val
    #         stack.append((node.left, curr_sum - node.val))
    #         stack.append((node.right, curr_sum - node.val))
    #     return False

    # bfs
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #     q = deque()
    #     q.append((root, sum))
    #     while q:
    #         node, curr_sum = q.popleft()
    #         if not node:
    #             continue
    #         if not node.left and not node.right:
    #             return curr_sum == node.val
    #         q.append((node.left, curr_sum - node.val))
    #         q.append((node.right, curr_sum - node.val))
    #     return False
