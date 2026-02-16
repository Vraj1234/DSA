class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        op = {'(', '{', '['}
        cl = {')', '}', ']'}
        for ch in s:
            if stack and ch in cl:
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        return False if stack else True
