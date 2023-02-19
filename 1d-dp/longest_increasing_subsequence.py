# Longest Increasing Subsequence (Medium)
# Link - https://leetcode.com/problems/longest-increasing-subsequence/

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.


class Solution:
    # dp solution, Time - O(n.n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            # check each next number
            for j in range(i+1, len(nums)):
                # if curr number is less than next numbers
                if nums[i] < nums[j]:
                    # store max LIS for "i" in dp
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

    # binary search solution, Time - O(nlogn)
    # def bs(self,l,r,lst,tr):
    #     pd=0
    #     while l<=r:
    #         mid=(l+r)//2
    #         if lst[mid]<tr:
    #             l=mid+1
    #         elif lst[mid]>tr:
    #             r=mid-1
    #             pd=mid
    #         else:
    #             pd=mid
    #             break
    #     return pd

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n=len(nums)
    #     lst=[]
    #     for i in range(n):
    #         if len(lst)==0 or nums[i]>lst[-1]:
    #             lst.append(nums[i])
    #         else:
    #             x=self.bs(0,len(lst)-1,lst,nums[i])
    #             lst[x]=nums[i]
    #     return len(lst)
