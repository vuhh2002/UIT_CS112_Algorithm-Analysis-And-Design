# https://leetcode.com/problems/word-search/
class Solution:
    def __init__(self):
        self.m = None
        self.n = None
    
    def exist(self, board, word):
        self.m = len(board)
        self.n = len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if word[0] == board[i][j] and self.search(board, word, i, j, 0):
                    return True
                
        return False

    def search(self, board, word, i, j, pos):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or word[pos] != board[i][j]:
            return False
        if pos == len(word) - 1:
            return True
        
        temp = board[i][j]
        board[i][j] = ' '
        res = self.search(board, word, i, j + 1, pos + 1) \
                or self.search(board, word, i, j - 1, pos + 1) \
                or self.search(board, word, i + 1, j, pos + 1) \
                or self.search(board, word, i - 1, j, pos + 1)
        board[i][j] = temp
        return res

    def solve(self, board, word):
        if self.exist(board, word):
            return "true"
        else:
            return "false"
    
    def getExtraInfo(self):
        return []


board = input()[3:-3].split("\'], [\'")
board = [a.split("\', \'") for a in board]
word = input()

if Solution().exist(board, word):
    print("true")
else:
    print("false")