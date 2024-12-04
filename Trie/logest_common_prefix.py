strs = ["flower","flow","flight"]

class TrieNode:
    def __init__(self):
        children = {}
        ew = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.childer:
                curr.children[letter] = TrieNode()
                curr = curr.children[letter]
        curr.ew += 1

    