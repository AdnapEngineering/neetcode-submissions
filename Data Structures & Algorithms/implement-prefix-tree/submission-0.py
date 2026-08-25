class TrieNode:
    def __init__(self):
        self.children = {}  # maps char -> TrieNode
        self.end_of_word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    ## start at the top, check each character exists in children and either add it or move to the child. At the end of the word set end_of_word to True
    def insert(self, word: str) -> None: 
        curr = self.root
        for c in word: 
            if c not in curr.children:
                curr.children[c] = TrieNode()    
            curr = curr.children[c]    
        curr.end_of_word = True

    # starts at root and checks for each char as children moving down the tree.
    # when at end of word, if node has end_of_word True, return True, anything else return False
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word 
        # starts at root, for every char in prefix, if it exists as children return True, else False
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix: 
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True    
        