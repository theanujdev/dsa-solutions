# Word Search II (Hard)
# Link - https://leetcode.com/problems/word-search-ii/

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example 1:
# Input: board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], words = ["oath", "pea", "eat", "rain"]
# Output: ["eat", "oath"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def remove_word(self, word):
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.add_word(word)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or board[r][c] not in node.children
                or (r, c) in visited
            ):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                trie.is_word = False
                res.add(word)

            if not node.children:
                del node
            else:
                dfs(r + 1, c, node, word)
                dfs(r - 1, c, node, word)
                dfs(r, c + 1, node, word)
                dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")

        return list(res)


# Solution 2
# class TrieNode:
#     def __init__(self):
#         self.children = collections.defaultdict(TrieNode)
#         self.is_word = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for c in word:
#             node = node.children[c]
#         node.is_word = True

# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         trie = Trie()
#         for w in words:
#             trie.insert(w)

#         m, n = len(board), len(board[0])
#         res = []
#         for i in range(m):
#             for j in range(n):
#                 paths = []
#                 path = ""
#                 self.dfs(board, i, j, trie.root, path, paths)
#                 res += paths
#         return res

#     def dfs(self, board, row, col, node, path, paths):
#         # match words starting from node of the trie, board starting from (row, col)
#         if node.is_word:
#             paths.append(path)
# 			# set to False so not to repeat the same word
#             node.is_word = False

#         m, n = len(board), len(board[0])
# 		# similar to two pointers: here is to check if pointer for board reaches its end, or not a match
#         if row < 0 or row >=m or col < 0 or col >= n or board[row][col] not in node.children:
#             return

# 		# This is similar to 2 pointers: now a match is found, move the pointer for trie and pointer for board
#         tmp = board[row][col]
#         board[row][col] = '#'
#         dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#         for d in dirs:
#             r, c = row + d[0], col + d[1]
#             self.dfs(board, r, c, node.children[tmp], path + tmp, paths)
#         board[row][col] = tmp

#         # pruning: if it is a leaf and a matched word is found for it already, pop it to decrease trie size
#         if len(node.children[tmp].children) == 0:
#             del node.children[tmp]
