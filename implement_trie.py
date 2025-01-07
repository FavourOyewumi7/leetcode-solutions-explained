"""
I believe this is a quite straightforward question and any one who has a good understanding of the Trie data structure can easily solve it.
"""
class TrieNode:
    def __init__(self, val = ''):
        self.wordend = False
        self.letters = [None]*26
class Trie:
    def __init__(self):
        self.root = TrieNode()
           
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.letters[index] == None:
                curr.letters[index] = TrieNode(w)
            curr = curr.letters[index]
        curr.wordend = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            index = ord(w) - ord('a')
            if curr.letters[index] == None:
                return False
            curr = curr.letters[index]
        if curr is not None and curr.wordend:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for p in prefix:
            index = ord(p) - ord('a')
            if curr.letters[index] == None:
                return False
            curr = curr.letters[index]
        if curr is not None:
            return True
        return False
