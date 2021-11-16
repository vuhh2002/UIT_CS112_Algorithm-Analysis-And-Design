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

    def search(self, board, word, row, col, pos):
        if row < 0 or row >= self.m or col < 0 or col >= self.n or word[pos] != board[row][col]:
            return False
        if pos == len(word) - 1:
            return True
        
        temp = board[row][col]
        board[row][col] = ' '
        res = self.search(board, word, row, col + 1, pos + 1) \
                or self.search(board, word, row, col - 1, pos + 1) \
                or self.search(board, word, row + 1, col, pos + 1) \
                or self.search(board, word, row - 1, col, pos + 1)
        board[row][col] = temp
        
        return res

    def solve(self, board, word):
        if self.exist(board, word):
            return "true"
        else:
            return "false"
    
    def getExtraInfo(self):
        return []


board = input().strip()[3:-3].split("\'], [\'")
board = [a.split("\', \'") for a in board]
word = input().strip()
Solution().solve(board, word)