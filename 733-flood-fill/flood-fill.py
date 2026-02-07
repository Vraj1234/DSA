class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        rows = len(image)
        cols = len(image[0])
        vis = [[False] * cols for _ in range(rows)]
        i,j = sr, sc
        original = image[i][j]

        # def bfs(i,j):
        #     q = deque()
        #     q.append([i,j])
        #     vis[i][j] = True

        #     while q:
        #         temp = []
        #         while q:
        #             temp.append(q.popleft())
        #         if i>=0 and i <rows and j>=0 and j < cols:
        #             if image[i][j-1] != color 



        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j] == color or vis[i][j] == True:
                return
            
            if image[i][j] == original:
                vis[i][j] = True
                image[i][j] = color
                dfs(i, j-1)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i+1, j)
        
        
        
        dfs(i,j)

        return image
