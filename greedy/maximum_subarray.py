# Maximum Subarray (Medium)
# Link - https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray[4, -1, 2, 1] has the largest sum 6.


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum = nums[0]
    #     curr_sum = 0
    #     for num in nums:
    #         if curr_sum<0:
    #             curr_sum = 0
    #         curr_sum += num
    #         max_sum = max(max_sum, curr_sum)
    #     return max_sum

    # def maxSubArray(self, nums: List[int]) -> int:
    #     newNum = maxTotal = nums[0]
    #     for i in range(1, len(nums)):
    #         newNum = max(nums[i], nums[i] + newNum)
    #         maxTotal = max(newNum, maxTotal)
    #     return maxTotal

    # dp solution
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, num in enumerate(nums):
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)
