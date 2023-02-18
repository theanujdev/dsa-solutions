# Jump Game (Medium)
# Link - https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2, 3, 1, 1, 4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    # greedy solution
    def canJump(self, nums: List[int]) -> bool:
        jumps_remaining = nums[0]
        for i in range(1, len(nums)):
            if jumps_remaining == 0:
                return False
            jumps_remaining = max(jumps_remaining-1, nums[i])
        return True

    # dp solution
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     dp = [True] + [False]*(n-1)
    #     for i in range(n):
    #         if dp[i]:
    #             # then we can travel up to index nums[i]+i
    #             s = nums[i]+i
    #             # if this is not enough to make it to the end of the array
    #             if s < n - 1:
    #                 # then update all indices from i+1 to s since we can reach them all from here
    #                 for j in range(i+1,s+1):
    #                     dp[j] = True
    #             # if we can reach the end of the array then return true
    #             else:
    #                 return True
    #     return False
