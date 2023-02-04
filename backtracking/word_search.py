# Word Search (Medium)
# Link - https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCCED"
# Output: true


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                    (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         if not board:
#             return False
#         h, w = len(board), len(board[0])
#         def dfs_search(idx: int, x: int, y: int) -> bool:
#             if x < 0 or x == w or y < 0 or y == h or word[idx] != board[y][x]:
#                 return False
#             if idx == len(word) - 1:
#                 return True
#             cur = board[y][x]
#             # mark as '#' to avoid repeated traversal
#             board[y][x] = '#'
#             # visit next four neighbor grids
#             found = dfs_search(idx + 1, x + 1, y) or dfs_search(idx + 1, x - 1, y) or dfs_search(idx + 1, x, y + 1) or dfs_search(idx + 1, x, y - 1)
#             # recover original grid character after DFS is completed
#             board[y][x] = cur
#             return found
#         return any(dfs_search(0, x, y) for y in range(h) for x in range(w))
