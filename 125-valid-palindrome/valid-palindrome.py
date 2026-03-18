class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(x.lower() for x in s if x.isalnum())
        print(clean)
        n = len(clean)-1
        l,r = 0, n
        while l<=r:
            if clean[l]!=clean[r]:
                return False
            l+=1
            r-=1
        return True