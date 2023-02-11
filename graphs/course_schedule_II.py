# Course Schedule II (Medium)
# Link - https://leetcode.com/problems/course-schedule-ii/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
# must take course bi first if you want to take course ai.

# - For example, the pair[0, 1], indicates that to take course 0 you have to first take course 1.

# Return the ordering of courses you should take to finish all courses. If there are many valid
# answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: [0, 1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
# course 0. So the correct course order is [0, 1].


from collections import defaultdict, deque


class Solution:
    # Solution 1
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        ans = []
        for c1, c2 in prerequisites:
            adj_list[c2].append(c1)
            indegree[c1] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        while q:
            node = q.popleft()
            ans.append(node)
            for vertex in adj_list[node]:
                indegree[vertex] -= 1
                if indegree[vertex] == 0:
                    q.append(vertex)

        if len(ans) == numCourses:
            return ans
        return []

    # Solution 2
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     adj = {c:set() for c in range(numCourses)}
    #     for c1, c2 in prerequisites:
    #         adj[c1].add(c2)

    #     visited, cycle = set(), set()
    #     ans = []

    #     def dfs(c):
    #         # cycle detected
    #         if c in cycle:
    #             return False
    #         if c in visited:
    #             return True
    #         cycle.add(c)
    #         visited.add(c)
    #         for pre in adj[c]:
    #             if not dfs(pre):
    #                 return False
    #         cycle.remove(c)
    #         ans.append(c)
    #         return True

    #     for c in range(numCourses):
    #         if not dfs(c):
    #             # cycle detected
    #             return []
    #     return ans
