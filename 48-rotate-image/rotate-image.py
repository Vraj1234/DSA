class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R,C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(r,C):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # print(matrix)
        for row in matrix:
            row.reverse()
        
    
