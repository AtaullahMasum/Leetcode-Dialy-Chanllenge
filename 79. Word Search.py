# if using hashset then data set reamin unchanged 
# using temp also correct answer but when return statement is true then main board is changed 
# so it is important to main board is unchanged so hashset is batter option than using temp
class Solution:
    def dfs(self, board, i, j, idx,  word, hashset):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx] or (i,j) in hashset:
            return False
        #temp , board[i][j] = board[i][j] , "#"
        hashset.add((i,j))
        if (self.dfs(board, i+1, j, idx+1, word, hashset) or
           self.dfs(board, i-1, j, idx+1, word, hashset) or
           self.dfs(board, i, j+1, idx+1, word, hashset) or 
           self.dfs(board, i, j-1, idx+1, word, hashset)):
           return True
        #board[i][j] = temp
        hashset.remove((i,j))
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashset = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, 0, word, hashset):
                    return True
        return False
        