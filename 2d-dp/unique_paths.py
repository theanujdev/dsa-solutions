# Unique Paths (Medium)
# Link - https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located at the top-left corner(i.e., grid[0][0]). The robot tries to move to the bottom-right corner(i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# Input: m = 3, n = 7
# Output: 28


class Solution:
    # 2d-dp
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for r in range(m-1):
            new_row = [1] * n
            for c in range(n-2, -1, -1):
                new_row[c] = new_row[c+1] + row[c]
            row = new_row
        return row[0]

    # dp (backtracking)
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dp = [[0]*101 for i in range(101)]  # input limit of 100
    #     def count(r,c):
    #         if r == 1 or c == 1:
    #             return 1
    #         if dp[r][c]:
    #             return dp[r][c]
    #         left = count(r - 1, c)
    #         right = count(r, c - 1)
    #         dp[r][c] = left + right
    #         return dp[r][c]
    #     return count(m,n)
