class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        R,C = len(board), len(board[0])
        vis = set()

        def dfs(r,c):
            if r<0 or r>=R or c<0 or c>=C or (r,c) in vis or board[r][c] == 'X':
                return
            
            vis.add((r,c))
            board[r][c] = 'T'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)


        for c in range(C):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[R-1][c] == 'O':
                dfs(R-1,c)

        for r in range(R):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][C-1] == 'O':
                dfs(r,C-1)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        
        
        

