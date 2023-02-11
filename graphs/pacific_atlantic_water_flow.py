# Pacific Atlantic Water Flow (Medium)
# Link - https://leetcode.com/problems/pacific-atlantic-water-flow/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate(r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell(ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:
# Input: heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
#     2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
# Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0, 4]: [0, 4] -> Pacific Ocean
# [0, 4] -> Atlantic Ocean
# [1, 3]: [1, 3] -> [0, 3] -> Pacific Ocean
# [1, 3] -> [1, 4] -> Atlantic Ocean
# [1, 4]: [1, 4] -> [1, 3] -> [0, 3] -> Pacific Ocean
# [1, 4] -> Atlantic Ocean
# [2, 2]: [2, 2] -> [1, 2] -> [0, 2] -> Pacific Ocean
# [2, 2] -> [2, 3] -> [2, 4] -> Atlantic Ocean
# [3, 0]: [3, 0] -> Pacific Ocean
# [3, 0] -> [4, 0] -> Atlantic Ocean
# [3, 1]: [3, 1] -> [3, 0] -> Pacific Ocean
# [3, 1] -> [4, 1] -> Atlantic Ocean
# [4, 0]: [4, 0] -> Pacific Ocean
# [4, 0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.


class Solution:
    # O(n) solution
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or
                    r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    heights[r][c] < prev_height
                    ):
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for r in range(rows):
            # traverse from first column
            dfs(r, 0, pac, heights[r][0])
            # traverse from last column
            dfs(r, cols-1, atl, heights[r][cols-1])

        for c in range(cols):
            # traverse from first row
            dfs(0, c, pac, heights[0][c])
            # traverse from last row
            dfs(rows-1, c, atl, heights[rows-1][c])

        # find common cells
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
