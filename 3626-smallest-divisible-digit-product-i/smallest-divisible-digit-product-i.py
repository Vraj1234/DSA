class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(n):
            res = 1
            while n:
                digit = n%10
                res = res*digit
                n = n//10
            
            return res

        for i in range(n,n+11):
            if digit_product(i)%t == 0:
                return i