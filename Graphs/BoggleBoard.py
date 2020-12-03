"""
Similar Qn --> Word Search II

"""

"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically or diagonally neighboring.
The same letter cell may not be used more than once in a word.

Input: board = [ ["o","a","a","n"],
                 ["e","t","a","e"],
                 ["i","h","k","r"],
                 ["i","f","l","v"] ]
                
       words = ["oath","pea","eat","rain"]
       
Output: ["eat","oath"]

"""
# Solution --> Little Different From AlgoExpert
# Time O(nm * 8^s + ws) | Space O(ws + nm)
----------------------
def BoggleBoard(board, words):
    trie = Trie()   # Look below for defintion
    for word in words:
        trie.add(word)
    
    res, seen = [], set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, board, trie, res, seen)
            
    return res

def dfs(i, j, board, node, res, seen):
    if node.end:
        res.append(node.end)
        node.end = False
        
    if outofBounds(i, j, board) or (i,j) in seen:
        return
    
    letter = board[i][j]
    if letter not in node.root:
        return 
    
    seen.add((i,j))
    node = node.root[letter]
    
    # horizontal and vertical
    dfs(i+1, j, board, node, seen, res)
    dfs(i-1, j, board, node, seen, res)
    dfs(i, j+1, board, node, seen, res)
    dfs(i, j-1, board, node, seen, res)
    #diagonal
    dfs(i-1, j-1, board, node, seen, res)
    dfs(i-1, j+1, board, node, seen, res)
    dfs(i+1, j+1, board, node, seen, res)
    dfs(i+1, j-1, board, node, seen, res)

    seen.remove((i,j))

    
def outofBound(i, j, board):
    return i < 0 or j < 0 or i >= len(board) or j >= len(board[i])

class Trie:
    def __init__(self):
        self.root = {}
        self.end = False
        
    def add(self, word):
        current = self
        for ch in word:
            if ch not in current.root:
                current.root[ch] = Trie()    # I am creating a Trie class, where as in algoExpert they creat only a dictionary
                
            current = current.root[ch]
            
        current.end = word  # We add the word, So we dont have to keep track of the word
        

            
            
            
            
            
            
        
