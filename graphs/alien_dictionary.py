# Alien Dictionary (Hard)
# Link - https://leetcode.com/problems/alien-dictionary/

# There is a new alien language that uses the English alphabet. However, the order among
# the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary, where the strings
# in words are sorted lexicographically by the rules of this new language.

# Return a string of the unique letters in the new alien language SOIted in lexicographically
# increasing order by the new language's rules. If there is no solution, return "". If there are
# multiple solutions, return any of them.

# A string 5 is lexicographically smaller than a string t if at the first letter where they
# differ, the letter in s comes before the letter in t in the alien language. If the first
# min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.1ength.

# Example 1:
# Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
# Output: "wertf"


class Solution:
    def alien_order(self, words):
        adj_list = {char: set() for word in words for char in word}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            # edge case: if same prefix but different len
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break

        # topological sort using post order dfs (reverse)
        visited = {}    # {char: bool} False - visited, True - in current path
        res = []  # in reverse order ans

        def dfs(c):
            if c in visited:
                # if in visited, returns True and indicates loop
                return visited[c]

            visited[c] = True

            for nei in adj_list[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)  # post order

        for char in adj_list:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(Solution().alien_order(words))
