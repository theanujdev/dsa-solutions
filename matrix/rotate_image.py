# Rotate Image (Medium)
# Link - https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees(clockwise).

# You have to rotate the image in -place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r-l):
                top, bottom = l, r
                # save top left value
                topLeft = matrix[top][l+i]
                # top left <- bottom left
                matrix[top][l+i] = matrix[bottom-i][l]
                # bottom left <- bottom right
                matrix[bottom-i][l] = matrix[bottom][r-i]
                # bottom right <- top right
                matrix[bottom][r-i] = matrix[top+i][r]
                # top right <- temp
                matrix[top+i][r] = topLeft
            l += 1
            r -= 1

    # pythonic - transpose and reverse
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     matrix[:] = [row[::-1] for row in list(zip(*matrix))]
