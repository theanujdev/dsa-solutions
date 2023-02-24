# Rectangle Overlap (Easy)
# Link - https://leetcode.com/problems/rectangle-overlap/

# An axis-aligned rectangle is represented as a list[x1, y1, x2, y2], where(x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

# Example 1:
# Input: rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3]
# Output: true


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x1, rec1_y1, rec1_x2, rec1_y2 = rec1
        rec2_x1, rec2_y1, rec2_x2, rec2_y2 = rec2

        overlap = rec1_x1 < rec2_x2 and rec1_y1 < rec2_y2 and rec1_x2 > rec2_x1 and rec1_y2 > rec2_y1

        return overlap
