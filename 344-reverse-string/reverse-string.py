class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recur(i,j):
            if i>=j:
                return
            
            s[i], s[j] = s[j], s[i]
            recur(i+1, j-1)
        
        recur(0, len(s)-1)
        return s

        