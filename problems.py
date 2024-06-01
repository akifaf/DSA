class TrieNode:

  def __init__(self):
    self.children = {}
    self.endOfWord = False

class Trie:

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    curr = self.root
    for letter in word:
      if letter not in curr.children:
        curr.children[letter] = TrieNode()
      curr = curr.children[letter]
    curr.endOfWord = True

  def search(self, word):
    curr = self.root
    for letter in word:
      if letter not in curr.children:
        return False
      curr = curr.children[letter]
    return True


class BST:
  
  def __init__(self, key):
    self.key = key
    self.lchild = None
    self.rchild = None

  def insert(self, data):
    if self.key is None:
      self.key = data
    if data < self.key:
      if self.lchild:
        self.lchild.insert(data)
      else:
        self.lchild = BST(data)
    if data > self.key:
      if self.rchild:
        self.rchild.insert(data)
      else:
        self.rchild = BST(data)
    
