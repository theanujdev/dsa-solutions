# Clone Graph (Medium)
# Link - https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.
# Return a deep copy(clone) of the graph.
# Each node in the graph contains a value(int) and a list(List[Node]) of its neighbors.

# class Node {
#     public int val
#     public List < Node > neighbors
# }

# Test case format:

# For simplicity, each node's value is the same as the node's index(1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Example 1:
# Input: adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
# Output: [[2, 4], [1, 3], [2, 4], [1, 3]]
# Explanation: There are 4 nodes in the graph.
# 1st node(val=1)'s neighbors are 2nd node(val=2) and 4th node(val=4).
# 2nd node(val=2)'s neighbors are 1st node(val=1) and 3rd node(val=3).
# 3rd node(val=3)'s neighbors are 2nd node(val=2) and 4th node(val=4).
# 4th node(val=4)'s neighbors are 1st node(val=1) and 3rd node(val=3).


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    # dfs solution
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        clones = {}

        def dfs(node):
            if node in clones:
                return clones[node]

            new_node = Node(node.val, [])
            clones[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)

    # bfs solution
    # def cloneGraph(self, node: 'Node') -> 'Node':
    #     if not node:
    #         return node
    #     q, clones = deque([node]), {node.val: Node(node.val, [])}

    #     while q:
    #         curr = q.popleft()
    #         curr_clone = clones[curr.val]
    #         for nei in curr.neighbors:
    #             if nei.val not in clones:
    #                 clones[nei.val] = Node(nei.val, [])
    #                 q.append(nei)
    #             curr_clone.neighbors.append(clones[nei.val])

    #     return clones[node.val]
