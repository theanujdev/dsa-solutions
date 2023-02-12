# Flood Fill (Easy)
# Link - https://leetcode.com/problems/flood-fill/

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels(also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2
# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
# Explanation: From the center of the image with position(sr, sc) = (1, 1)(i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel(i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        replace_color = image[sr][sc]

        def dfs(r, c):
            if (r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    image[r][c] == color or
                    image[r][c] != replace_color
                    ):
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
