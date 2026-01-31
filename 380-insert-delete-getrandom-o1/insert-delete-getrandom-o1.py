class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.ls = []

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.mp[val] = len(self.ls)
            self.ls.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.mp:
            pos = self.mp[val]
            self.ls[-1], self.ls[pos] = self.ls[pos], self.ls[-1]
            self.mp[self.ls[pos]] = pos 
            self.mp.pop(val, 0)
            self.ls.pop()
            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self.ls)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()