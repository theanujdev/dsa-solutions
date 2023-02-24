# Rectangle Area (Medium)
# Link - https://leetcode.com/problems/rectangle-area/

# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner(ax1, ay1) and its top-right corner(ax2, ay2).

# The second rectangle is defined by its bottom-left corner(bx1, by1) and its top-right corner(bx2, by2).

# Example 1:
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # function to caculate area of rectangle (Length * width)
        def area(x1, y1, x2, y2):
            return (x2-x1)*(y2-y1)

        # finding the overlap rectangle length and width
        overlapX = max(min(ax2, bx2)-max(ax1, bx1), 0)
        overlapY = max(min(ay2, by2)-max(ay1, by1), 0)

        # area1 + area2 - Overlap Rectangle Area
        return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - overlapX * overlapY
