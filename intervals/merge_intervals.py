# Merge Intervals (Medium)
# Link - https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals[1, 3] and [2, 6] overlap, merge them into[1, 6].


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            # if overlap, merge by updating last end
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res

    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     res = []
    #     for interval in sorted(intervals, key=lambda i: i[0]):
    #         if res and interval[0] <= res[-1][1]:
    #             res[-1][1] = max(res[-1][1], interval[1])
    #         else:
    #             res += [interval]
    #     return res
