# Encode and Decode Strings (Medium)
# Link - https://www.lintcode.com/problem/659/

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Please implement encode and decode

# Example 1

# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is : "lint:;code:;love:;you"


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + s
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        res = []
        string = ""
        str_len = 0
        for s in str:
            if str_len == 0:
                if string != "":
                    res.append(string)
                    string = ""
                str_len = int(s)
                continue
            string += s
            str_len -= 1
        res.append(string)
        return res


strs = ["we", "say", ":", "yes"]
encoded_str = Solution().encode(strs)
print("encoded str :", encoded_str)
decoded_str = Solution().decode(encoded_str)
print("decoded str :", decoded_str)
