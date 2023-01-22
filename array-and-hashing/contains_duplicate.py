# Contains Duplicate (Easy)
# Link - https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true


class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))
