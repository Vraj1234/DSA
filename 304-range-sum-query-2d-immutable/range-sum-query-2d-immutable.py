class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R,C = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0]*(C) for _ in range(R)]

        for r in range(R):
            running_sum = 0
            for c in range(C):
                running_sum += matrix[r][c]
                if r>0:
                    running_sum += self.prefix_matrix[r-1][c]
                self.prefix_matrix[r][c] = running_sum
                if r>0:
                    running_sum -= self.prefix_matrix[r-1][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        BR = self.prefix_matrix[row2][col2]
        TR_minus_one = 0 if row1 == 0 else self.prefix_matrix[row1-1][col2]
        BL_minus_one = 0 if col1 == 0 else self.prefix_matrix[row2][col1-1]
        TL_minus_one_both = 0 if row1 == 0 or col1==0 else self.prefix_matrix[row1-1][col1-1]
        return BR-TR_minus_one-BL_minus_one+TL_minus_one_both


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)