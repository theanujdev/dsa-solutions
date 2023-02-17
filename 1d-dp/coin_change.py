# Coin Change (Medium)
# Link - https://leetcode.com/problems/coin-change/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1


class Solution:
    # dp bottom-up (Tabulation)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(1, amount+1):
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[amount] if dp[amount] != amount + 1 else -1

    # dp top-down (Memoization)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     def dfs(rem, cache):
    #         if rem < 0:
    #             return math.inf
    #         if rem == 0:
    #             return 0
    #         if rem in cache:
    #             return cache[rem]

    #         cache[rem] = min(dfs(rem-c, cache) + 1 for c in coins)
    #         return cache[rem]

    #     ans = dfs(amount, {})
    #     return -1 if ans == math.inf else ans
