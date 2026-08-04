class Solution:
    def checkValidString(self, s: str) -> bool:
        mn, mx = 0,0
        for ch in s:
            if ch == "(":
                mn+=1
                mx+=1
            if ch == ")":
                mn-=1
                mx-=1
            if ch == "*":
                mn-=1
                mx+=1
            if mx<0:
                return False
            if mn<0:
                mn = 0
            
        return mn ==0