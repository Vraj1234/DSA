class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x in "+-/*":
                denom = stack.pop()
                num = stack.pop()
                if x == "+":
                    stack.append(denom+num)
                if x == "-":
                    stack.append(num-denom)
                if x == "*":
                    stack.append(denom*num)
                if x == "/":
                    stack.append(int(num/denom))
            else:
                stack.append(int(x))
        
        return stack[-1]
