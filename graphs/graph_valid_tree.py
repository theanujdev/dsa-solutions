# Graph Valid Tree (Medium)
# Link - https://www.lintcode.com/problem/178/

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges(each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

# Example 1:
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj_list = {i: set() for i in range(n)}
        for n1, n2 in edges:
            adj_list[n1].add(n2)
            adj_list[n2].add(n1)
        visited = set()

        def dfs(curr, prev):
            # loop detected
            if curr in visited:
                return False
            visited.add(curr)
            for nei in adj_list[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True

        # true if no loop tree and all nodes are connected
        return dfs(0, -1) and n == len(visited)
