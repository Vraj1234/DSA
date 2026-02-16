class RandomizedSet:

    def __init__(self):
        self.umap = {}
        self.ls = []
        self.i = 0

    
    def insert(self, val: int) -> bool:
        if val in self.umap:
            return False
        else:
            self.umap[val] = self.i
            self.ls.append(val)
            self.i+=1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.umap:
            f_index = self.umap[val]
            s_index = self.umap[self.ls[-1]]
            self.umap[val] = s_index
            self.umap[self.ls[-1]] = f_index
            self.ls[f_index], self.ls[s_index] = self.ls[s_index], self.ls[f_index]
            self.ls.pop()
            del self.umap[val]
            self.i-=1
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        random_number = random.randint(0, len(self.ls)-1)
        return self.ls[random_number]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()