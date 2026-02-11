class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        extra = 0
        e_open = set()
        e_close = set()
        for i,x in enumerate(s):
            if x == '(':
                open_count+=1
                e_open.add(i)
            if x == ")":
                if open_count!= 0:
                    open_count-=1
                    e_open.pop()
                else:
                    extra+=1
                    e_close.add(i)

        res = ""
        for i,x in enumerate(s):
            if i not in e_open and i not in e_close:
                res+=x
        
        return res
