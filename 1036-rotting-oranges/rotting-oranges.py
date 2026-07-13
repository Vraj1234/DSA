class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        freshOranges = 0

        R,C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    freshOranges+=1
        if freshOranges == 0:
            return 0
        time = 0
        while q:
            l = len(q)
            for i in range(l):
                r,c = q.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        freshOranges-=1
            time+=1

        return -1 if freshOranges else time-1
