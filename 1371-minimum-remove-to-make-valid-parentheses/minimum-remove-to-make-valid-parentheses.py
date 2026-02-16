class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        extra = []
        for i,ch in enumerate(s):
            if ch == '(':
                stack.append((ch,i))
            if ch == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    extra.append((ch,i))
        
        s_st = set([x[1] for x in stack])
        e_st = set([x[1] for x in extra])
        res = ""
        for i,x in enumerate(s):
            if i not in s_st and i not in e_st:
                res+=x
        
        return res
            
        
                 
            