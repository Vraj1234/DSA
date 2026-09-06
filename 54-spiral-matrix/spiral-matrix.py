class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        l = 0
        r = C-1
        t = 0
        b = R-1
        i = 0

        res = []
        
        while l<=r and t<=b:
            i = l
            while l<=r and t<=b and i <= r:
                res.append(matrix[t][i])
                i+=1
            t+=1

            i = t
            while l<=r and t<=b and i <= b:
                res.append(matrix[i][r])
                i+=1
            r-=1

            i = r
            while l<=r and t<=b and i >= l:
                res.append(matrix[b][i])
                i-=1
            b-=1

            i = b
            while l<=r and t<=b and i>= t:
                res.append(matrix[i][l])
                i-=1
            l+=1 
        
        return res