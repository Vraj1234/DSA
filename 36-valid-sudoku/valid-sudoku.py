class Solution:
    def isValidSudoku(self, grid: List[List[str]]) -> bool:
        R,C = len(grid), len(grid[0])
        umap = defaultdict(set)
        for i in range(3):
            for j in range(3):
                umap[(i,j)] = set()

        for r in range(R):
            rc_set = set()
            for c in range(C):
                v = grid[r][c]
                if v!= ".":
                    if v in rc_set:
                        return False
                    else:
                        rc_set.add(v)
            rc_set.clear()

        for c in range(C):
            rc_set = set()
            for r in range(R):
                v = grid[r][c]
                if v!= ".":
                    if v in rc_set:
                        return False
                    else:
                        rc_set.add(v)
            rc_set.clear()
        
        for r in range(R):
            for c in range(C):
                v = grid[r][c]
                if v != ".":
                    if v in umap[(r//3, c//3)]:
                        return False
                    umap[(r//3, c//3)].add(v)
        
        return True

