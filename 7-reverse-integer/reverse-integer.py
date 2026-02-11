class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31-1
        

        sign = -1 if x<0 else 1
        x = abs(x)
        res = 0

        while x:
            digit = x%10
            x = x//10
            if res > INT_MAX//10:
                return 0
            
            elif res == INT_MAX//10 and digit > INT_MAX%10:
                return 0
            
            else:
                res = res*10 + digit
        
        return res*sign