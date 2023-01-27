# Valid Parentheses (Easy)
# Link - https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        stack = []
        for char in s:
            if char in hashmap:
                if len(stack) == 0 or hashmap[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return True if len(stack) == 0 else False


s = "(]"
print(Solution().isValid(s))
