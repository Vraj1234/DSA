class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        stack = []
        for ch in s:
            if ch.isnumeric():
                if stack and stack[-1].isnumeric():
                    stack[-1] = str(int(stack[-1])*10 + int(ch))
                    continue
            if ch == "]":
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                temp.reverse()
                num = int(stack.pop())
                if not stack:
                    res.extend(temp * num)
                else:
                    stack.extend(temp * num)
            else:
                stack.append(ch)
        
        temp = []
        while stack:
            temp.append(stack.pop())
        
        temp.reverse()
        res.extend(temp)

        return "".join(res)