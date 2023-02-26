# Counting Bits (Easy)
# Link - https://leetcode.com/problems/counting-bits/

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10


class Solution:
    # dp solution, Time - O(n)
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    # def countBits(self, num: int) -> List[int]:
    #     counter = [0]
    #     for i in range(1, num+1):
    #         counter.append(counter[i >> 1] + i % 2)
    #     return counter
