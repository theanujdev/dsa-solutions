# Reverse Integer (Medium)
# Link - https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers(signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x *= sign
        while x:
            rev = rev * 10 + x % 10
            x = x // 10
        rev *= sign
        # check if 32-bit int
        if rev < -(2**31) or rev > (2**31 - 1):
            return 0
        return rev

    # def reverse(self, x: int) -> int:
    #     MIN = -2**31     # -2147483648
    #     MAX = 2**31 - 1   # 2147483647
    #     res = 0
    #     while x:
    #         digit = int(math.fmod(x, 10))  # (python dumb) -1 %  10 = 9
    #         x = int(x / 10)  # (python dumb) -1 // 10 = -1
    #         if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
    #             return 0
    #         if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
    #             return 0
    #         res = (res * 10) + digit
    #     return res
