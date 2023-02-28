# Meeting Rooms (Easy)
# Link - https://www.lintcode.com/problem/920/

# Given an array of meeting time intervals consisting of start and end times[[s1, e1], [s2, e2], ...](si < ei), determine if a person could attend all meetings.

# (0, 8), (8, 10) is not conflict at 8

# Example 1:
# Input: intervals = [(0, 30), (5, 10), (15, 20)]
# Output: false
# Explanation:
# (0, 30), (5, 10) and (0, 30), (15, 20) will conflict


class Solution:
    def can_attend_meetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                return False
            prev_end = end
        return True


intervals = [(0, 30), (5, 10), (15, 20)]
print(Solution().can_attend_meetings(intervals))
