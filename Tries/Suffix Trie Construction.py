"""
Construct a Suffix Trie
"""

Class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endsymbol = '*'
        self.populateSuffixTrie(string)
     
    # O(N^2) Time and Space
    def populateSuffixTrie(self, string):
        for i in range(len(string)):
            self.insertSubStringStarting(i, string)
            
    def insertSubStringStarting(self, ind, string):
        node = self.root
        for j in range(ind, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
            
        node[self.endsymbol] = True
    
    # O(N) Time | O(1) Space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
            
        return self.endsymbol in node
            
  
