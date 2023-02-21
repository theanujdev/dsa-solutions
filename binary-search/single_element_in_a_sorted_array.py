# Single Element in a Sorted Array (Medium)
# Link - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

# Example 1:
# Input: nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# Output: 2


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            # get even length on both sides
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]
