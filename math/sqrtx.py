# Sqrt(x) (Easy)
# Link - https://leetcode.com/problems/sqrtx/

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while r >= l:
            mid = (l+r)//2
            if mid*mid <= x:
                l = mid+1
            else:
                r = mid-1
        return r

    # def mySqrt(self, x):
    #     l, r = 0, x
    #     while l <= r:
    #         mid = (l+r)//2
    #         square = mid * mid
    #         if (square <= x) and ((mid+1)*(mid+1) > x):
    #             return mid
    #         elif square > x:
    #             r = mid - 1
    #         else:
    #             l = mid + 1

    # def mySqrt(self, x: int) -> int:
    #     num = 0
    #     while True:
    #         square = num*num
    #         if square==x:
    #             return num
    #         elif square>x:
    #             return num-1
    #         num+=1
