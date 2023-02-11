# Course Schedule (Medium)
# Link - https://leetcode.com/problems/course-schedule/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# - For example, the pair[0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.


class Solution:
    # dfs O(V+E) solution
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: set() for i in range(numCourses)}
        for c1, c2 in prerequisites:
            adj_list[c1].add(c2)
        visited = set()

        def canFinishCourse(c):
            # detect cycle
            if c in visited:
                return False
            if adj_list[c] == []:
                return True
            visited.add(c)
            for pre in adj_list[c]:
                if not canFinishCourse(pre):
                    return False
            visited.remove(c)
            adj_list[c] = []
            return True

        for c in range(numCourses):
            if not canFinishCourse(c):
                return False
        return True

    # topological sort
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     adj = {i:set() for i in range(numCourses)}
    #     indegree = [0] * numCourses
    #     stack = []

    #     for c1, c2 in prerequisites:
    #         adj[c2].add(c1)
    #         indegree[c1] += 1

    #     for i in range(numCourses):
    #         if indegree[i] == 0:
    #             stack.append(i)

    #     count = 0
    #     while stack:
    #         node = stack.pop()
    #         count += 1
    #         for adj_vertex in adj[node]:
    #             indegree[adj_vertex] -= 1
    #             if indegree[adj_vertex] == 0:
    #                 stack.append(adj_vertex)

    #     return count == numCourses

    # bfs solution
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     todo = {i: set() for i in range(numCourses)}
    #     graph = defaultdict(set)
    #     for i,j in prerequisites:
    #         todo[i].add(j)
    #         graph[j].add(i)
    #     q = deque([])
    #     for k,v in todo.items():
    #         if len(v) == 0:
    #             q.append(k)
    #     while q:
    #         n = q.popleft()
    #         for i in graph[n]:
    #             todo[i].remove(n)
    #             if len(todo[i]) == 0:
    #                 q.append(i)
    #         todo.pop(n)
    #     return not todo
