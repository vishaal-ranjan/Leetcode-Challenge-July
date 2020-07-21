class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.explore(board, word, i, j, m, n):
                        return True
                    
        return False
    
    def explore(self, board, word, i, j, m, n):
        if len(word) == 0:
            return True
        
        # check corner conditions
        if i < 0 or i == m or j < 0 or j == n or board[i][j] != word[0]:
            return False
        
        # mark the element
        board[i][j] = '#'
        
        # we will explore in all 4 directions
        
        if self.explore(board, word[1:], i+1, j, m, n):
            return True
        if self.explore(board, word[1:], i, j+1, m, n):
            return True
        if self.explore(board, word[1:], i-1, j, m, n):
            return True
        if self.explore(board, word[1:], i, j-1, m, n):
            return True
        
        board[i][j] = word[0]
        
        return False