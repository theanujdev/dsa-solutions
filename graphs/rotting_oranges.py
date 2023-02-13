# Rotting Oranges (Medium)
# Link - https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:

# - 0 representing an empty cell,
# - 1 representing a fresh orange, or
# - 2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4


class Solution:
    # bfs solution
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh_oranges = 0, 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh_oranges > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nc < 0 or
                                nr >= rows or nc >= cols or
                                grid[nr][nc] != 1
                            ):
                        continue
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append((nr, nc))
            time += 1

        return time if fresh_oranges == 0 else -1
