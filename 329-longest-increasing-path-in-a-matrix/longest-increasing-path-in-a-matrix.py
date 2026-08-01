class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        vis = set()
        dp = [[-1]*C for _ in range(R)]
        res = float('-inf')

                        
                    
                    
        def dfs(r,c, prevr, prevc):
            if r<0 or r>=R or c<0 or c>=C:
                return 0
            if prevr != -1 and matrix[r][c] <= matrix[prevr][prevc]:
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            res = 1 + max(dfs(r-1,c,r,c),dfs(r+1,c,r,c),dfs(r,c-1,r,c),dfs(r,c+1,r,c))
            dp[r][c] = res 
            return res
            

        for r in range(R):
            for c in range(C):
                res = max(res, dfs(r,c, -1, -1))
        
        # SC = O(mxn) + O(m+n) 
        # TC = O(mxn)
        return res