# Climbing Stairs (Easy)
# Link - https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


class Solution:
    # optimized dp (bottom-up)
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

    # dp (bottom-up)
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     dp = [-1] * (n + 1)  # to accomodate for 0-based indexing
    #     dp[1], dp[2] = 1, 2
    #     for i in range(3, n + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #     return dp[n]

    # memoization dp (top-down)
    # def climbStairs(self, n: int) -> int:
    #     def climb(n):
    #         if n in memo:
    #             return memo[n]
    #         else:
    #             memo[n] = climb(n-1) + climb(n-2)
    #             return memo[n]
    #     memo = {1: 1, 2: 2}
    #     return climb(n)

    # naive recursion
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     else:
    #         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
