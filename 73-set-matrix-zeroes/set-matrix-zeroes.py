class Solution:
    def setZeroes(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R,C = len(grid), len(grid[0])
        first_row_zero = False
        first_col_zero = False
        for r in range(R):
            if grid[r][0] == 0:
                first_col_zero = True
                break
        
        for c in range(C):
            if grid[0][c] == 0:
                first_row_zero = True
                break
        
        for r in range(1, R):
            for c in range(1, C):
                if grid[r][c] == 0:
                    grid[r][0] = 0
                    grid[0][c] = 0

        for r in range(1, R):
            for c in range(1, C):
                if grid[r][0] == 0 or grid[0][c] == 0:
                    grid[r][c] = 0
        
        if first_row_zero:
            for c in range(C):
                grid[0][c] = 0
            
        if first_col_zero:
            for r in range(R):
                grid[r][0] = 0