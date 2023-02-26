# Missing Number (Easy)
# Link - https://leetcode.com/problems/missing-number/

# Given an array nums containing n distinct numbers in the range[0, n], return
# the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3, 0, 1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range[0, 3]. 2 is the missing number in the range since it does not appear in nums.


class Solution:
    # Sum method, Time - O(n), Space - O(1)
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += i - nums[i]
        return res

    # binary solution, Time - O(n), Space - O(1)
    # def missingNumber(self, nums: List[int]) -> int:
    #     res = len(nums)
    #     for i in range(len(nums)):
    #         res ^= i ^ nums[i]
    #     return res

    # Sorting method, Time - O(nlogn), Space - O(1)
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums.sort()
    #     for i in range(len(nums)):
    #         if i != nums[i]:
    #             return i
    #     return nums[-1] + 1

    # Hashmap method, Time - O(n), Space - O(n)
    # def missingNumber(self, nums: List[int]) -> int:
    #     hashmap = set(nums)
    #     for i in range(len(nums)+1):
    #         if i not in hashmap:
    #             return i
