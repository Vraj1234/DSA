class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        vis = [[False]* cols for _ in range(rows)]
        arr = 0

        def dfs(i, j, arr):
            if i < 0 or i >= rows or j<0 or j>= cols or board[i][j] != word[arr] or vis[i][j] == True:
                return False

            vis[i][j] = True
            if(arr == len(word)-1):
                return True
            else:
                arr+=1

            if (dfs(i, j-1, arr) or dfs(i, j+1, arr) or dfs(i-1, j, arr) or dfs(i+1, j, arr)):
                return True

            vis[i][j] = False
            return False

        for i in range(rows):
            for j in range (cols):
                if board[i][j] == word[arr]:
                    if dfs(i,j,arr):
                        return True

        return False
        