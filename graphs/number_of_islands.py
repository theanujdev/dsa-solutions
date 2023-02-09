# Number of Islands (Medium)
# Link - https://leetcode.com/problems/number-of-islands/

# Given an m x n 2D binary grid grid which represents a map of '1's(land) and '0's(water),
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1


class Solution:
    # Solution 1
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # base conditions
            if (r < 0 or c < 0 or r == rows or c == cols):
                return
            if grid[r][c] != "1":
                return
            # mark cell visited
            grid[r][c] = "V"
            # dfs on adjacent cells
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands

    # Solution 2
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid or not grid[0]:
    #         return 0
    #     ROWS, COLS = len(grid), len(grid[0])
    #     visited = set()
    #     islands = 0
    #     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    #     def dfs(r, c):
    #         if (r<0 or c<0 or
    #             r>=ROWS or c>=COLS or
    #             grid[r][c] == "0" or
    #             (r, c) in visited
    #             ):
    #             return
    #         visited.add((r, c))
    #         for dr, dc in directions:
    #             dfs(r + dr, c + dc)

    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if grid[r][c] == "1" and (r, c) not in visited:
    #                 islands += 1
    #                 dfs(r, c)
    #     return islands
