class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.l = [""]*n
        self.size = n
    

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.l[idKey-1] = value
        if idKey>self.ptr:
            
            return []
        else:
            while self.ptr<= self.size and self.l[self.ptr-1]!= "":
                res.append(self.l[self.ptr-1])
                self.ptr += 1
                
            return res


        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)