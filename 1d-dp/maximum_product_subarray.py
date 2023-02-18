# Maximum Product Subarray (Medium)
# Link - https://leetcode.com/problems/maximum-product-subarray/

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2, 3, -2, 4]
# Output: 6
# Explanation: [2, 3] has the largest product 6.


class Solution:
    # dp solution
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = 1, 1
        for n in nums:
            vals = (n*curr_max, n*curr_min, n)
            curr_max = max(vals)
            curr_min = min(vals)
            res = max(res, curr_max)
        return res

    # def maxProduct(self, nums: List[int]) -> int:
    #     prefix, suffix, max_so_far = 0, 0, float('-inf')
    #     for i in range(len(nums)):
    #         prefix = (prefix or 1) * nums[i]
    #         suffix = (suffix or 1) * nums[~i]  # -i - 1
    #         max_so_far = max(max_so_far, prefix, suffix)
    #     return max_so_far
