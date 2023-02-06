# Set Matrix Zeroes (Medium)
# Link - https://leetcode.com/problems/set-matrix-zeroes/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# Input: matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


class Solution:
    # Time - O(m.n), Space - O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        is_row_zero = False
        # iterate through matrix to mark the zero rows and cols
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        is_row_zero = True
        # iterate through matrix to update the zero rows and cols
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # update the first col if it's zero
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        # update the first row if it's zero
        if is_row_zero:
            for c in range(COLS):
                matrix[0][c] = 0

    # Time - O(m.n), Space - O(m+n)
    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     ROWS, COLS = len(matrix), len(matrix[0])
    #     r_zero, c_zero = set(), set()
    #     # add rows and cols with zero
    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if matrix[r][c]==0:
    #                 r_zero.add(r)
    #                 c_zero.add(c)
    #     # iterate and mark zeros in matrix
    #     for r in range(ROWS):
    #         for c in range(COLS):
    #             if r in r_zero or c in c_zero:
    #                 matrix[r][c] = 0
