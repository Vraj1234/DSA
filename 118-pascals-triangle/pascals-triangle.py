class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        first = [1]
        second = [1,1]
        res = []
        res.append(first[:])
        if numRows == 1:
            return res
        res.append(second[:])
        if numRows == 2:
            return res

        i = 2
        while i < numRows:
            first[:] = second
            second.clear()
            second.append(1)
            prev = 1
            for f in range(len(first)-1):
                j = f+1
                second.append(first[f]+ first[j])
            second.append(1)
            # print("at ", i ,"appending: ", second)
            res.append(second[:]) 
            i+=1
        
        return res