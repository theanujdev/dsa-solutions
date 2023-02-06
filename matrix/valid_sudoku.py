# Valid Sudoku (Medium)
# Link - https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# - A Sudoku board(partially filled) could be valid but is not necessarily solvable.
# - Only the filled cells need to be validated according to the mentioned rules.

# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true


from collections import defaultdict


class Solution:
    # Solution 1
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".":
                    continue
                if (curr in rows[r] or
                        curr in cols[c] or
                        curr in squares[(r//3, c//3)]
                        ):
                    return False
                rows[r].add(curr)
                cols[c].add(curr)
                squares[(r//3, c//3)].add(curr)
        return True

    # Solution 2
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     # check rows
    #     for i in range(9):
    #         seen = set()
    #         for j in range(9):
    #             curr = board[i][j]
    #             if curr == '.':
    #                 continue
    #             if curr in seen:
    #                 return False
    #             seen.add(curr)
    #     # check columns
    #     for j in range(9):
    #         seen = set()
    #         for i in range(9):
    #             curr = board[i][j]
    #             if curr == '.':
    #                 continue
    #             if curr in seen:
    #                 return False
    #             seen.add(curr)
    #     # check sub squares
    #     for i in range(3):
    #         for j in range(3):
    #             seen = set()
    #             for r in range(i*3,i*3+3):
    #                 for c in range(j*3,j*3+3):
    #                     curr = board[r][c]
    #                     if curr == '.':
    #                         continue
    #                     if curr in seen:
    #                         return False
    #                     seen.add(curr)
    #     return True
