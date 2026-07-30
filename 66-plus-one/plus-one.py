class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        for i in range(n-1, -1, -1):
            new = digits[i] + carry
            carry = 0
            if i == n-1:
                new+=1
            if new > 9:
                digits[i] = new%10
                carry = 1
            else:
                digits[i] = new
                break
                
        if carry == 1:
            digits.insert(0,1)
        return digits