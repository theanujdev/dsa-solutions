# Product of Array Except Self (Medium)
# Link - https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]


class Solution:
    def productExceptSelf(self, nums):
        # answer array doesn't count towards space complexity
        ans = [1]*len(nums)
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            ans[i] *= prefix           # prefix product from one end
            prefix *= nums[i]
            ans[-1-i] *= postfix       # suffix product from other end
            postfix *= nums[-1-i]
        return ans


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
