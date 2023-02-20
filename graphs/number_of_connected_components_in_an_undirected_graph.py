# Number of Connected Components In An Undirected Graph (Medium)
# Link - https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# You have a graph of n nodes. You are given an integer n and an array edges where
# edges[i] = [ab, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[6, 1], [1, 2], [3, 4]]
# Output: 2


class Solution:
    # union find solution
    def countComponents(self, n: int, edges) -> int:
        par = [i for i in range(n)]
        rank = [1] * n  # for optimization

        def find(n):
            res = n
            while res != par[res]:
                par[res] = par[par[res]]  # path compression optimize
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # find parent nodes

            if p1 == p2:  # already joint
                return 0

            # join nodes (union)
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(Solution().countComponents(n, edges))
