class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {}
        res = []

        def calc(x):
            original = x
            power = 0
            temp = []
            temp.append(original)
            while x!= 1:
                if cache.get(x, 0) != 0:
                    power+=cache[x]
                    break
                elif x%2 == 0:
                    x = x//2
                    power+=1
                    temp.append(x)
                else:
                    x = 3*x + 1
                    temp.append(x)
                    power+=1
            
            res.append((original, power))

            for x in temp:
                cache[x] = power
                power-=1

        for x in range(lo, hi+1):
            calc(x)

        res.sort(key = lambda x: (x[1], x[0]))
        print(res)
        res2 = [x[0] for x in res]
        print(res2)
        return res2[k-1]