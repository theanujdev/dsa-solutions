# Non-overlapping Intervals (Medium)
# Link - https://leetcode.com/problems/non-overlapping-intervals/

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# Output: 1
# Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            # if not overlap, update prev end
            if start >= prev_end:
                prev_end = end
            else:
                count += 1
                # preserve short interval, deleted bigger
                prev_end = min(prev_end, end)

        return count
