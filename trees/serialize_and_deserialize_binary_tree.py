# Serialize and Deserialize Binary Tree (Hard)
# Link - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example 1:
# Input: root = [1, 2, 3, null, null, 4, 5]
# Output: [1, 2, 3, null, null, 4, 5]


from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                return res.append("N")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(data.split(","))

        def dfs():
            val = data.popleft()
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

    # def deserialize(self, data):
    #     data = data.split(',')
    #     self.i = 0
    #     def dfs():
    #         if data[self.i] == 'N':
    #             self.i += 1
    #             return None
    #         root = TreeNode(int(data[self.i]))
    #         self.i += 1
    #         root.left = dfs()
    #         root.right = dfs()
    #         return root
    #     return dfs()

    # def serialize(self, root):
    #     if not root:
    #         return "N"
    #     t = f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
    #     print(t)
    #     return t

    # def deserialize(self, data: str):
    #     return self.deserialize_list(data.split(","))

    # def deserialize_list(self, nums: List[str]):
    #     val = nums.pop(0)
    #     if val=="N":
    #         return None
    #     root = TreeNode(val)
    #     root.left = self.deserialize_list(nums)
    #     root.right = self.deserialize_list(nums)
    #     return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
