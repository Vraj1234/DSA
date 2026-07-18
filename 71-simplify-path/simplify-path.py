class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        res = []
        stack = []
        for e in components:
            if e == "..":
                if stack:
                    stack.pop()
            elif e == "." or e == "":
                continue
            else:
                stack.append(e)
        
        res.append("/")
        for st in stack:
            res.append(st)
            res.append("/")
        
        if stack:
            res.pop()
        
        return "".join(res)
        


