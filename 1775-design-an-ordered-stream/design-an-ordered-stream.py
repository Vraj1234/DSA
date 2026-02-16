class OrderedStream:

    def __init__(self, n: int):
        self.ls = [""]*(n+1)
        self.ptr = 1
        self.size = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey] = value
        res = []
        while self.ptr <= self.size and self.ls[self.ptr] != "":
            res.append(self.ls[self.ptr])
            self.ptr+=1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)