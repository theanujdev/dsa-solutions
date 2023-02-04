# Design Add and Search Words Data Structure (Medium)
# Link - https://leetcode.com/problems/design-add-and-search-words-data-structure/

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

# Example 1:
# Input
# ["WordDictionary", "addWord", "addWord", "addWord",
#     "search", "search", "search", "search"]
# [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
# Output
# [null, null, null, null, false, true, true, true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# wordDictionary.search("pad")
# // return False
# wordDictionary.search("bad")
# // return True
# wordDictionary.search(".ad")
# // return True
# wordDictionary.search("b..")
# // return True


# Solution 1
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            curr = root
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for trie in curr.children.values():
                        if dfs(trie, i+1):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.end
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Solution 2
# from collections import defaultdict


# class WordDictionary:
#     def __init__(self):
#         self.words = defaultdict(set)

#     def addWord(self, word: str) -> None:
#         self.words[len(word)].add(word)

#     def search(self, word: str) -> bool:
#         for other in self.words[len(word)]:
#             any_mismatch = any(word[x] != '.' and word[x] != other[x] for x in range(len(word)))
#             if not any_mismatch:
#                 return True
#         return False
