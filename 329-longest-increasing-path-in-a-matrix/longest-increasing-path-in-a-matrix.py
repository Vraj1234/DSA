class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        vis = set()
        dp = [[-1]*C for _ in range(R)]
        res = 0
        def dfs(r,c, prevr, prevc):
            if r<0 or r>=R or c<0 or c>=C:
                return 0 
            
            if (r,c) in vis:
                return 0
            
            if prevr!= -1 and matrix[r][c] <= matrix[prevr][prevc]:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
                
            vis.add((r,c))
             #right
            res =  1 + max( dfs(r-1, c, r, c), dfs(r+1, c, r, c), dfs(r, c-1, r, c), dfs(r, c+1, r, c))
            vis.remove((r,c))
            dp[r][c] = res
            return res
            
        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r,c, -1, -1))
        
        return res