class MyStack:

    def __init__(self):
        self.q = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.top_element = x

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            e = self.q.popleft()
            self.q.append(e)
            self.top_element = e
        return self.q.popleft()
        

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()