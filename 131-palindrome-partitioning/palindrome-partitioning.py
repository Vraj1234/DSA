class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        temp = ""
        temp_ls = []
        def check_palindrome(s):
            if len(s)==0:
                return False
            return s== s[::-1]

        def bt(start):
            if start == len(s):
                res.append(temp_ls[:])
                return
            
            for i in range(start, len(s)):
                temp = s[start:i+1]
                if check_palindrome(temp):
                    temp_ls.append(temp)
                    bt(i+1)
                    temp_ls.pop()
                
        
        bt(0)
        return res
            
