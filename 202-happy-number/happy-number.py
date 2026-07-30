class Solution:
    def isHappy(self, n: int) -> bool:
        done = set()
        num = n

        def sum_of_squares(number):
            res = 0
            while number:
                digit = number%10
                res = res + (digit*digit)
                number = number//10
            return res
        
        while num !=1 and num not in done:
            done.add(num)
            num = sum_of_squares(num)
        
        print(done)
        if num in done:
            return False
        
        return True