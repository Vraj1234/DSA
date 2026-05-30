class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = ""

        def bt(l, count_o, count_c, temp):
            if l == n*2:
                res.append(temp[:])
                return
            
            if count_o > count_c:
                if count_o < n:
                    temp+="("
                    bt(l+1, count_o+1, count_c, temp)
                    temp = temp[:-1]
                temp+=")"
                bt(l+1, count_o, count_c+1, temp)
                temp = temp[:-1]
                
            else:
                temp+="("
                bt(l+1, count_o+1, count_c, temp)
                temp = temp[:-1]
            
        bt(0,0,0, temp)
        return res