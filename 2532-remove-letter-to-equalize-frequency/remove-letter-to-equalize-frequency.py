class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        ls= list(c.values())
        for i in range(len(ls)):
            temp = ls[:]
            temp[i] -=1
            if temp[i] == 0:
                temp.pop(i)
            if len(set(temp)) == 1:
                return True
        return False



        
